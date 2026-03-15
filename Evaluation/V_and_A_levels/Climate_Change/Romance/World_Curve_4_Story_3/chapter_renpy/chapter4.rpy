label chapter4:

    # [Scene: The Beacon Plaza | Evening]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, steady strings under a hopeful piano motif]
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls, murmured conversation, rain tapping a slow tempo on the plaza canopy]
    "You arrive with the compass in your palm the way you always do—an old weight that centers you when the world feels like a ledger of losses. You felt the decision at the meeting in your"
    "chest hours ago; choosing the public route wasn't effortless, but it felt right. It felt like doing the thing you were raised to do: speak with hands and show where the next hands could join you."
    "The stage smells faintly of wet wood and printer ink. Your hair is in a messy bun; a stray tendril keeps falling into your face and you push it back, thumb brushing the salt at your"
    "temple. Noah stands just behind you, fingers curled around a roll of maps, his presence low and steady like a tide at the far edge of hearing. He doesn't tell you what to do—he never does—but"
    "he looks at you now in a way that asks, Will you do this with me?"
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You don't have to carry the whole town, Asha. I'll—' (he fumbles for the right word) '—I'll carry the approvals if you'll carry the plan."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We carry it together. You shepherd the signatures; I shepherd the soil."
    hide noah_reyes
    hide asha_moreno

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A few appreciative murmurs like pebbles tipping in a tray]
    "You begin with the image that matters most: the marsh as living architecture. You point to the rib of cordgrass in the drawing."
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "These reed beds are more than plants. They're living breakwaters—each stem a tiny engineer. If we stitch marsh restoration to a sensor network we control, we get early warnings and a living buffer. We get jobs, we get stewardship, and we keep this shoreline commons in our hands."
    show marta_chen at right:
        zoom 0.7

    marta_chen "That's what we've been saying! People can garden and also guard the line. Let them teach the sensors our ways."

    asha_moreno "Exactly. Community crews tend the marsh and the sensors. We train volunteers to read data and soil tests. The clause I proposed in the funding agreement guarantees that sensor data remains governed by us—not a private feed that disappears behind a corporate lock."

    menu:
        "Open with a short memory about your father at the boatyard":
            "You let the crowd see the small, human hinge of why this matters: your father's hands, a lost boat, and the stubborn grammar of repair. The room goes softer; a few faces you know wrinkle with recognition."
        "Lead with technical models and numbers":
            "You draw out the projection graphs, point to a curve of storm frequency and the buffer gains. Engineers near the back nod; a practical hum runs through the crowd. The argument lands with the people who listen to evidence."

    # --- merge ---
    "..."
    "Noah Reyes steps forward when you gesture to the municipal approval you need."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "I've been in the hallways. I've had meetings. I've seen the budget line items. I'll push this through council if you lead the implementation. We'll make that clause non-negotiable. We'll make it visible—permissions, audits, local hosts for the feeds."

    asha_moreno "And we'll recruit volunteers, set training times, embed the sensors in community workdays. Eli's boat crew can help with the platforms; Marta's gardens can test salinity treatments. This is not top-down. It's patchwork in the best sense—neighbors patching what the sea unravels."
    "Eli, standing with his arms folded and a smudge of sawdust still on his cheek, steps up with a slow, approving nod."
    hide asha_moreno
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "If you plan it so the boats and the beds can both breathe, I'm in. You show me how to anchor the platforms and I'm building."
    "The crowd begins to hum—part cheer, part the steady stitch of agreement. Lila watches from the edge of the plaza, hands folded in a practiced clap. Her applause is measured, polite; it carries the sheen of someone cataloguing the optics."
    hide marta_chen
    show lila_park at right:
        zoom 0.7

    lila_park "This is a strong community narrative. I admire that. Partnerships are—useful.' (she inclines her head, eyes flicking to Noah then to you) 'We can fund pilots. We can scale. The Beacon will be a hub for monitoring—there's a lot of value in centralization."
    "You sense the economy in the word value, and you know exactly where her priorities sit. Still, she surprised you tonight by clapping when the crowd clapped—anathema as it is to reduce someone to applause alone. Her face is unreadable in the way that matters: complex, yes, but not hostile."
    hide noah_reyes
    show asha_moreno at center:
        zoom 0.7

    asha_moreno "We welcome collaboration. We also insist on terms that keep control here—community governance over the data and any expansion. That's not a marginal ask. It's essential."
    # play music "music_placeholder"  # [Music: Strings swell gently, brightening]
    # play sound "sfx_placeholder"  # [Sound: Applause rises, solid and warm]
    "A town elder—a voice cracked by weather and candor—raises a hand."

    "Elder" "What if the sensors fail? What if the marsh takes longer? Will this leave us worse off?"
    "You pause. You could recite models; you could promise certainty. Instead you say what you always come back to."

    asha_moreno "We don't have certainty. We have people who have kept each other alive for generations. We have work that's repairable. The marshwork is slow by design—it's a long investment—but the citizen-run sensors mean when something shifts, we know sooner. We learn faster together. We can pilot, adapt, and refuse to sell what keeps us home."
    hide eli_duarte
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "And we'll set up a binding review—six months, twelve months—where the community reviews sensor governance and program outcomes. We make the funding provisional until those benchmarks are met."
    "Another round of cheering. Marta's laughter cuts through like a ribbon."
    hide lila_park
    show marta_chen at right:
        zoom 0.7

    marta_chen "Volunteer signups at the table! Seedlings and sensors!"
    "You step down from the stage as neighbors swarm to the tables, fingerprints bright on flyers and clasped hands passing volunteer sign-up sheets. The practical hum of people deciding to do things—signing, pointing, arguing gently over schedules—feels like the strongest kind of vote."

    menu:
        "Find Noah and press your hand to his arm, wordless":
            "You press your palm to his forearm. He looks at you, surprised into a half-smile, and squeezes back. There's a small, private gravity between you that says, We're doing this."
        "Head straight to the volunteer table and start assigning teams":
            "You pull a clipboard into your hands and begin pairing people by skills—gardeners with boat-hands, electricians with students. The rush of organization steadies you; the town hums into motion."

    # --- merge ---
    "..."
    "Later, under the promontory lights of the Beacon throwing a calm halo above the water, the celebration spills onto the Promenade. Wooden boards steam in the cool mist, and people embrace—wet hugs that smell of salt"
    "and frying dough. Eli cracks a grin as he hooks his arm around an old friend; Marta drags two teenagers into a group photo, cheeks flushed."
    "You move through the crowd, the compass still tucked in your hand like a small litany. A volunteer hands you a paper cup of something warm; steam curls up with the smell of citrus and spice."
    "Noah Reyes finds you where the promenade narrows, waves a hand, and draws you toward the railing. The sea reflects the Beacon's halo in fractured silver."

    noah_reyes "They voted provisional funding. Mayor Rosa signed the clause verbally in front of her aides. It's not final paperwork, but it matters. They heard you."
    "Asha Moreno: (you want to say more than the protocol says; you want to stitch the night into the next morning) 'It matters because people showed up. You held the approvals so I could stand in front of them and ask for the work.'"

    noah_reyes "We did it together. And—' (he hesitates, like he's choosing a non-political truth) '—I know what's at risk for you in pushing it publicly. The Beacon smelled like a tribunal tonight. But you gave them a way to belong to the solution."
    "You feel the swell of something hot and steady beneath your ribs: gratitude, relief, and a soft fear that is not paralyzing but bright with possibility."
    # [Scene: Tidewatch Lab | Late Night]
    hide asha_moreno
    hide noah_reyes
    hide marta_chen

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, single-note motifs echoing the evening's resolve]
    # play sound "sfx_placeholder"  # [Sound: The soft buzz of a monitor, rain on the lab roof like fingers drumming a patient rhythm]
    "Back inside Tidewatch, the lab smells of ozone and damp paper. Your hands fold around the brass compass as if to remind yourself that you are allowed to have steady things. Noah sets down the rolled maps, now unrolled and annotated, and settles into a chipped stool opposite you."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "We should sleep. There are signatures to collect tomorrow and meetings.' (he rubs his palms together) 'But—' (he looks up) '—can I tell you a thing that has nothing to do with the council?"
    "You tilt your head. There are so many things he could say—small confessions, small promises."

    noah_reyes "When I was a kid, my sister used to leave a burned corner on a map. She said burned edges reminded her of where they'd been, so she wouldn't lose where she was going.' (he chuckles) 'I found one of her old city maps in a box last winter. It's folded up in my sketchbook."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "That sounds like a map that knew its story."

    noah_reyes "I want to help you keep this town's story on the map. Not just the safe bits—the messy, stubborn parts too.' He meets your gaze with a straightforwardness that displaces policy talk entirely. 'I will push for municipal approval. I will be blunt when it's time. I will stand in rooms and say your name when you can't. Will you let me?"
    "You could answer with a juridical agreement, a plan, a list. Instead you lift the compass and tuck it into your palm, letting the familiar weight be the word you need. It says steadiness. It says home. It says, I am anchored."

    asha_moreno "Yes."
    "Noah Reyes smiles, a slow thing that starts at his eyes and reaches his mouth. He reaches out and brushes a thumb over your hand, a contact that is not public policy and not a contract—just a quick, human covenant."
    # play music "music_placeholder"  # [Music: The piano resolves into a calm, hopeful chord]
    # play sound "sfx_placeholder"  # [Sound: A distant horn from the harbor, low and conciliatory]
    "You sit in the glow of the lab, maps spread, volunteer lists ticking over, the Beacon halo far off but tangible in the night. The town's future no longer feels like an abstraction; it feels like"
    "a project of hands and shared days. Your chest eases in a way it hasn't in months. For a moment the weight of responsibility is a kind of light you can carry."
    "A page-turning thought slides into focus: this surge—this public push—is not an end. It's the first tide of many you'll have to learn to read, steer, and sometimes withstand. But tonight, you have allies, a clause"
    "that preserves your community's voice, and a partner who will walk through the municipal rooms with you."
    "You tuck the brass compass fully into your palm, feeling the cold, familiar metal against your skin—steady, true. This is the surge you're meant to ride."
    hide noah_reyes
    hide asha_moreno

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a single sustained note that invites continuation]

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
