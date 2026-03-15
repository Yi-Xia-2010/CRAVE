label chapter2:

    # [Scene: Tidal Conservatory | Late Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft harp arpeggios under warm synth pads — hopeful, gently propulsive]
    # play sound "sfx_placeholder"  # [Sound: Slow drip, distant gull call, the faint whine of a humidity regulator]
    "Narration"
    "You step off the boardwalk and into a pocket of warmth. The Conservatory swallows the coastal chill and exhales a humid, green-scented breath; your jacket fogs the nearest pane as you move past a bed of"
    "halophytes that look defiant in their salt-glossed leaves. Your satchel — maps, meeting notes, the weight of tonight — rests against your hip like a familiar ache. From the stairwell you can already hear metallic walkways"
    "creak: the building's bones settle into their own rhythm, patient as a tide."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Condensation beads sliding, soft metallic creak]
    "Narration"
    "Dr. Linh is at the far table, sleeves rolled, hair holding droplets at the nape. She looks up as you approach and, without fanfare, extends a small vial of brackish water. The liquid catches the muted light — brown-green, flecked with suspended sediment."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Here. We sampled the new marsh patch this morning. Notice the particulate load — it's lower where the seagrass density increased. The models align with the wave-attenuation figures I sent you."
    "Narration"
    "You lift the vial, fingers cool on glass. Salt tang and wet earth rise in the seam between your nostrils and memory. Linh's voice is steady, calibrated; she trusts numbers the way some people trust weathered wood."
    show aria_marin at right:
        zoom 0.7

    aria_marin "It smells... alive.' (You tilt the vial, watching micro-swirls.) 'Those attenuation figures — what margin are we looking at for a mid-storm surge? For the boardwalk zone?"

    dr_linh_pham "Conservatively, a thirty to forty percent reduction in initial wave force with established beds. If we phase it in—seed, anchor, community maintenance—we see compounded gains over five years. Not immediate like a seawall, but resilient."
    "Narration"
    "Her measured cadence gives your plan a quiet scaffolding. You can feel the threads of it — the phased shorelines, the town fund, the volunteer brigades — fitting together beneath your skin. Yet the memory flickers:"
    "zoning maps, a storm two towns over, families displaced when concrete promises outpaced community time. Your palm tightens around a thin silver band in your pocket and then releases it like a confession."

    menu:
        "Hold the vial and ask Linh a technical question":
            "You keep the vial up to the light, letting the mist smear your eyelashes. 'If we stagger plots by neighborhood and account for seasonal sediment flows, could we accelerate colonization?' Linh's eyes flash; she launches into a short, eager outline of pilot plots and volunteer windows, and you feel the neatness of the plan slide into place."
        "Return the vial and change the subject to the town fund":
            "You hand the vial back, fingers brushing Linh's. 'Funding — the town will ask how we'll measure impact for allocations.' Linh frowns, then smiles with the warmth of an ally who knows grant language; she enumerates metrics and community monitoring protocols, and the practical next steps begin to ring like a bell."

    # --- merge ---
    "After either response, the team sharpens plans and exchange shifts to community engagement as Maya arrives."
    "Narration"
    "The choices you make with your attention matter less here than the fact that attention is paid. Before Linh finishes, the door shoves inward and Maya arrives like a living splash of color — blue raincoat"
    "liberally paint-splattered, palms smeared with teal. She slings a rolled mural plan under her arm and grins, breathless with the kind of energy that moves walls and hearts in equal measure."
    show maya_marin at center:
        zoom 0.7

    maya_marin "Aria! You won't believe how it reads — teal waves through the shops, the old 'Boardwalk' sign stitched into the mural like a memory you can touch. If people see it, they remember why they're staying."
    "Narration"
    "She spreads the sketch on the metal table: broad strokes of community faces caught in tide lines, a ribbon of sea-glass green curling through the composition. The paint is almost wet enough to steam."

    aria_marin "It’s beautiful, Maya. It anchors people to place."

    maya_marin "Exactly. Art's not just decoration. It's... claim-staking with color. If they can see what they'd lose, they'll fight for it differently."

    dr_linh_pham "There’s evidence that place-based art increases civic participation. If we tie installation to volunteer planting days, we get cross-pollination — literally and figuratively."
    "Narration"
    "Her words land like a second plank added to a makeshift bridge. You want to say yes, to stitch art and marsh and monitoring into one community heartbeat. Before you can, the Conservatory door shakes again."
    "Kai slips in, half-smile, curls dark and slightly damp, beads of salt on his jacket like punctuation."
    hide dr_linh_pham
    hide aria_marin
    hide maya_marin

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant clang of a dropped wrench from an outside crew — a tiny, human clatter]
    show kai_solano at left:
        zoom 0.7

    kai_solano "Miss me? I rallied a crew at the pier for tape and saws. We could start tonight — banners, a flash teach-in, then plant after tide recedes."
    "Narration"
    "His amber eyes catch yours and hold; the grin is familiar and disarming. You feel the lists in your satchel press against your ribs like a second heart. There is so much you want to give"
    "Kai in return — a warm salute, a laugh, a reckless answer — but the satchel's weight is a different kind of gravity. You return a tight, professional smile instead."
    show aria_marin at right:
        zoom 0.7

    aria_marin "Kai. I— I appreciate the energy. I want structured volunteer windows, trained crews, safety oversight. If people plant before the beds are prepped, we risk compaction and failure."

    kai_solano "Structures are fine where structures matter. But people need to feel they can act. Waiting for perfect conditions is how things get lost to committees."
    "Narration"
    "The exchange tightens into a familiar friction: your methodical scaffolding versus his kinetic insistence. It is not simply tactics. It smells of deeper philosophies — trust in institutions and slow-building consensus versus trust in the people's"
    "raw ability to remake things now. Your throat presses with the memory of past zoning maps and families forced to abandon houses they loved."

    aria_marin "No one is asking to wait forever. Phases with immediate, visible actions — art, small pilot beds, emergency training — that’s how we maintain momentum and accountability."

    kai_solano "That sounds like a promise I can work with. But promises need to be loud. They need to be felt in the streets."
    show dr_linh_pham at center:
        zoom 0.7

    dr_linh_pham "And they need frameworks. If we coordinate the loud moments with ecological windows, we multiply both impact and safety."
    hide kai_solano
    show maya_marin at left:
        zoom 0.7

    maya_marin "We can do both. Launch the mural as a call-to-action the night before planting. The mural lights the way; the beds catch the tide. People come for the art, they leave with soil on their hands."
    "Narration"
    "You listen to them — to Linh's calm models, Maya's creative insistence, Kai's urgent cadence — and you feel the plan settling into a shape that borrows strengths from each of them. It is not pristine;"
    "it is porous and human, a hybrid that could hold people and place together. You let out a breath that tastes of sea spray and possibility."

    menu:
        "Match Kai's volume with an impassioned call":
            "You stand a fraction more upright, voice carrying over the hum. 'Then we'll make this visible and accountable. Rally nights with project leads posted, a town fund contribution match, trained crew sign-ups. Let it be loud — but let it be measured.' Kai grins like you handed him a flag; Maya hugs the mural plan to her chest. Linh gives a reserved, pleased nod."
        "Double-down on procedural detail, pull out your notes":
            "You unzip your satchel and smooth a page of bullet points — timelines, metrics, funding brackets. 'Phase one: pilot plots in three neighborhoods, two community murals as call points, volunteer training schedule.' The room leans into the outline; Kai frowns, the spark of impatience flickering, but Linh relaxes, and Maya starts ticking items off with paint-stained fingers."

    # --- merge ---
    "Regardless of tone, the group coalesces around a combined plan of visible action plus structured oversight."
    "Narration"
    "There is an almost audible loosening in the Conservatory atmosphere as your words bind to theirs. Each of you has read the town's losses in different printings; each of you holds a piece of what preservation"
    "must be. The ring in your pocket presses against the soft pad of your palm again — not an accusation this time, but a reminder that choices have histories and that histories can be mended, slowly."
    hide aria_marin
    show kai_solano at right:
        zoom 0.7

    kai_solano "I don't want your plan to be 'compromise' in the way that sacrifices names on lists. If we do this, we do it with people in the room making the rules."
    hide dr_linh_pham
    show aria_marin at center:
        zoom 0.7

    aria_marin "I don't either. That's why community oversight is built into the fund's governance — seats for neighborhood reps, rotating facilitation, open audits."
    hide maya_marin
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "And Linh Labs will publish baseline and follow-up monitoring. Transparency isn't a buzzword here; it's how we verify that living shorelines produce the claimed benefits."
    hide kai_solano
    show maya_marin at right:
        zoom 0.7

    maya_marin "And art gets archived in the project log. Every mural, every volunteer photo tagged — proof of who held this place."
    "Narration"
    "For a beat, the Conservatory hums in consonance. It is a small, true music: people aligning on purpose. Outside, gulls wheel and the sea murmurs against distant pilings; inside, the halves of a plan begin to"
    "approximate a whole. You feel something rise — not certainty, but the warmer, steadier current of hope."
    hide aria_marin
    hide dr_linh_pham
    hide maya_marin

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft crescendo in the music; a single, bright piano chord]
    "Narration"
    "You look at each face: Linh's pragmatic concentration, Maya's luminous belief, Kai's guarded, fierce loyalty. You want to hold this portrait — a community choosing work over resignation — and carry it straight up to the rooftop where tonight's meeting will test whether belief can be translated into coalition."
    "Narration — Page-Turn Moment"
    "You fold the sketch from Maya near the edge of the table and slide a printed timeline under it, letting art and schedule breathe side by side. Outside the Conservatory, the afternoon shifts toward the long,"
    "storm-light blue that catches on Salthaven's edges. Your palms are still warm from the vial; the silver band in your pocket is cool. Hope feels like careful scaffolding built with many hands. You gather the satchel,"
    "the mural roll, Linh's summary printout, and step toward the exit with the plan forming like a tide-line you can follow."

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Hopeful strings swell, then soften]
    # play sound "sfx_placeholder"  # [Sound: Metallic creak of the doorway; distant community voices, a child's laugh carried on wind]

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
