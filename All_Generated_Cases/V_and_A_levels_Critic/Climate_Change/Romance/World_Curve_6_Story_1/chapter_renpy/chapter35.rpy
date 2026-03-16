label chapter35:

    # [Scene: Nueva Mar Municipal Hall | Late Morning]

    scene bg ch14_612518_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The mechanical hum of HVAC, punctuated by muffled voices and a distant siren]
    # play music "music_placeholder"  # [Music: Fast staccato strings under a low, insistent percussion — tension rising]
    "You arrive carrying an armful of binders that smell faintly of salt and printer toner. Your name is scrawled on more than one table assignment; your face is expected in rooms you have not slept through"
    "for weeks. The municipal hall feels smaller and farther away at once — a building that should be steady and anchor-like, now vibrating with deadlines."
    "You feel the motion of a thousand small crises: fund managers on the line, legal counsels quibbling over phrasing, engineers recalibrating trigger levels. Every paper you set down feels like a lever; every lever promises to"
    "tilt someone’s life. The negative weight of those promises presses against your sternum like ocean wind against a door."

    scene bg ch14_612518_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft scratch of a pen; an elevator sighs open]
    # play music "music_placeholder"  # [Music: Percussion quickens]
    "Elias Kahn slips into the room beside you as if he belongs to both the hall and the harbor. He carries a municipal tablet, his expression an even line that tightens when he looks at you."
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "They pushed the legal team again. Mayor Velez wants cleaner trigger language, and—' (he swallows) '—the finance office is asking for a three-year sunset on the monitoring fund unless we can prove outcomes faster."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "A sunset clause gives them a highway to walk away when audits get boring.' (You close your eyes for a second; the bright draft of the atrium brushes your face.) 'If the fund disappears after three years, all our oversight becomes paperwork and photo ops while the wall does the talking."

    elias_kahn "I know.' (He moves closer; there's a tremor to his voice that doesn't match his usual steadiness.) 'I'm pushing on the budget committee. I can argue for an endowment — tie it to port revenue — but they'll want guarantees, Maya. They want measurable, short-term metrics."

    maya_corvin "Measurable metrics are easy to bend.' (Your fingers find the trefoil beneath your sleeve; the metal is cold and steadies you.) 'We need thresholds that matter to people: flood-days reduced, wetlands restored, replacement housing guaranteed."

    elias_kahn "And audits scheduled with community seats on the board.' (He meets your eyes.) 'I put your draft language into the municipal packet."

    maya_corvin "You did that?"

    elias_kahn "I did. It won't pass unchanged, but it's there. I accepted a formal role on the oversight task force to shepherd the changes.' (He pauses, letting the admission hang.) 'It means I'll be in municipal meetings more. I wanted you to hear that from me."
    "You taste salt on your tongue and something like relief flashes — brief and brittle. Relief is invasive here; it asks for reciprocation even when everything else demands vigilance."

    maya_corvin "You're taking a municipal post."

    elias_kahn "I'm trying to be where the levers are.' (He gives you a small, lopsided smile.) 'I'm trying to keep the promise we made when this started."

    maya_corvin "We?' (Your tone is sharper than intended.) 'We made different promises once. You, me, everyone on the roofs and porches. I'm not sure municipal hall and porchlight are the same place."

    elias_kahn "They're not.' (He steps back, pragmatic now.) 'But maybe they can overlap. I can't change the systems from outside them."
    "You want to argue until your voice is raw. Instead you pivot to the only thing that steadies you professionally: data."

    maya_corvin "Where's Dr. Sima?"

    elias_kahn "In the lab with the latest tidal models. She's—' (he exhales) '—saying the buffered corridors must be at least three times wider than the model predicted if we want to hedge for extreme events. That changes cost projections. It will force us to prioritize."

    maya_corvin "Prioritize what—wetland corridor over promenade mosaics? Garden plots over a playground?' (Your voice tightens; the list of things you would save and the things you wouldn't could fill pages.) 'Make them choose, Elias. Make them see what their choice does to the people who live here."

    elias_kahn "They already see it as line-items. We have to translate it into duties. Legal obligations. Municipal and independent oversight with real teeth."

    maya_corvin "And the teeth will be enforced by who? A board that reads minutes and files reports?"

    elias_kahn "A board with community, municipal, and technical seats and a legal mandate. With funding tied to enforcement metrics. With an independent auditor."
    "You imagine the board forming: faces you know and faces you don't, an uneasy table where Rafi drinks bitter coffee beside a municipal lawyer and a stern auditor. You imagine formal minutes from which life cannot be unmade — legal scaffolding around fragile things."
    hide elias_kahn
    hide maya_corvin

    scene bg ch14_612518_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low electronic chirp as models load]
    # play music "music_placeholder"  # [Music: A rising, urgent string line]
    show dr_sima_raza at left:
        zoom 0.7

    dr_sima_raza "The waters we're modeling in twenty years are already here in storm surge scenarios. The corridors reduce wave energy, but to be effective they must be continuous and legally protected. The technical recommendation is non-negotiable."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Non-negotiable for science, negotiable for politics.' (You glare at the tidal map.) 'How much corridor do we need versus how much of the promenade becomes a sacrificial plaza?"

    dr_sima_raza "Enough to keep critical zones connected. Not everything can be saved in the old form. Some heritage sites can be integrated as adaptive spaces — movable mosaics, raised memorial platforms — but they will not be as they were."
    "The word 'not' lands like a slab. Negative certainty — a different mood than fear — settles into your bones."

    menu:
        "Speak first in the oversight meeting":
            "You raise your hand before Elias can. Your voice is rough but practiced as you begin to frame the community's demands. Heads turn; some expect drama, others notebooking. You feel exposed and fierce."
        "Let Elias open the meeting":
            "You let Elias step into the spotlight. He speaks in measured sentences, translating anger into policy. Relief and suspicion co-mingle in your chest as you watch him defend your language to strangers."

    menu:
        "Walk the line with Kai to inspect insertion points":
            "You stride along the scaffolding beside Kai, feeling the tremor of machinery through your boots. You ask pointed technical questions; she answers in clipped detail. Your hands tremble when you touch the metal — both because of adrenaline and the raw feel of construction."
        "Return to town and race the audit deadline":
            "You turn away from the wall, toward the thought of models and municipal clocks. Your feet kick up wet sand as you move; your throat is tight with the knowledge that legal instruments must be perfected before the next tide."

    menu:
        "Take the data packet to the finance committee yourself":
            "You wrap the printouts in plastic and run. The city at night is a blur of lights and anxious thumbs on screens. You arrive breathless and deliver the packets like a plea."
        "Let Elias present the packet, stay to marshal volunteers":
            "You stay on the roof, organizing volunteers into a visible cohort. You feel the tension braid into purpose as neighbors gather with clipboards and lamps. Elias is the bridge in the halls; you are the anchor among the people."

    jump chapter52
    return
