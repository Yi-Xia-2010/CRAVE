label chapter3:

    # [Scene: Marabel Promenade | Late afternoon — sky low with threat of rain]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a lowboard creak as people shuffle into place]
    # play music "music_placeholder"  # [Music: Soft, steady strings — hopeful, attentive]
    "You stand where the Promenade broadens into the municipal meeting area, the compass a small, familiar weight against your palm. Last chapter's momentum — the ledger, the lab, Noah's patient steadiness — folds into this moment"
    "like a map into your pocket. The air tastes of iron and salt; rain hangs in the clouds like a promise and a threat at once."
    "You breathe in, counting the small things: the scent of frying fish from a nearby stall, Marta's bright gardening gloves catching the light, Eli's palm leaving an oily print on a shipping crate he drums with"
    "restless rhythm. Mayor Rosa is already seated on the raised bench, braid coiled against her neck, hands threaded together as if they could stitch the town's frayed edges. Around you, neighbors cluster in wet jackets, umbrellas"
    "half-closed, faces open and expectant."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft, professional hum from the Beacon's demo case as PR staff set up a minimalist display]
    # play music "music_placeholder"  # [Music: A clean piano motif, precise]
    "Lila moves with the practiced grace of someone used to cameras and stage lights. Her PR team arrays a sleek tablet and a compact sensor rig — silent, proprietary; the display blinks with tidy graphs: predicted"
    "flood-lines, sensor feeds, a rendered wall that hugs Marabel like a white tooth against the water. Her voice when she speaks is clear as glass."
    show lila_park at left:
        zoom 0.7

    lila_park "Marabel doesn't need another pilot project. It needs infrastructure you can count on. Scalable sea walls, floating platforms for critical services, and a sensor network monitored in real time. Investment, job creation, and — most importantly — guarantees."
    "Her smile is calibrated to the crowd; the promise is simple, immediate, attractive. People lean forward. The Beacon's demo flickers: real-time tide models, a simulated storm surge held at bay by engineered plates."
    "Mayor Rosa: (softly) 'Guaranteed how, Lila? Grants, loans, maintenance costs? Ownership—?'"

    lila_park "Public-private partnership. We'll fund the initial capital. We'll train local teams to operate the systems. We propose a multi-year maintenance contract. The consortium takes the lead; the town benefits."
    "Your chest tightens at 'consortium' and 'take the lead'—phrases that feel like fingers closing on property lines. But you keep the ledger under your arm and stand up, because you promised yourself you'd speak in both technical terms and human ones."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Mayor Rosa, neighbors — thank you. I appreciate the scale of the offer. I think scalable infrastructure can be part of the solution, but it shouldn't replace local stewardship. My proposal is a hybrid: marsh restoration to absorb storm energy, community-operated sensors that feed into any wall system, and a matching fund structure so ownership stays local."
    "You feel the words landing differently than you rehearsed them. They're not as tight as Lila's pitch, not as glossy, but they carry weight you trust—soil, seedbeds, and the stubbornness of people who have lived with the tide for generations."
    "Marta Chen: (sharp, immediate) 'Community-operated sensors. That's not negotiable. If the data's locked behind a corporate firewall, we lose our voice.'"
    "Eli Duarte: (hitting the crate once) 'We need to keep the boatyards, the kids' houses, the old docks. Ain't no wall that remembers how to call off a storm like the marsh does when it's healthy.'"
    "Noah Reyes rises slowly, palms open as if smoothing the air between people."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "We aren't here to torpedo investment. What Asha's proposing is a bridge. It lets us test restoration at scale while leveraging funds. We can draft governance terms that require open access to sensor data and local oversight of maintenance, Asha—if Lila's consortium agrees. That way, we secure short-term protection without relinquishing control."
    "Noah's voice is a tether. It looks to the room for consensus, then finds you; his eyes—deep, earnest—find you twice too many times, and your chest gives a small, involuntary answer. Hope flickers in the way he frames the bridge. It's cautious, reasonable, ready for negotiation."
    "Lila inclines her head, expression measured."

    lila_park "Open-data is an admirable ideal. It creates liabilities, security concerns, and inconsistent maintenance. Our model protects residents by ensuring uptime and effectiveness. Compromises introduce failure points."
    "She looks at you then, her steel-gray gaze appraising. It is not unkind; it is analytical, the look of someone running variables through a model and deciding which to keep. You are in her calculus."

    asha_moreno "If uptime is the concern, then guarantee language goes both ways. Performance bonds. Local maintenance capacity-building. An independent oversight board that includes Mayor Rosa, Marta, and community representatives. We agree on metrics before we install."
    "Mayor Rosa rubs the bridge of her nose, the braid in her hair catching the light as she shifts. Her face reads tired, but not defeat; someone who knows every choice costs something. She speaks slowly."
    hide lila_park
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "We need safety, yes. Fast. But we also need stability for families who can't afford another displacement. I want options that are immediate and that leave us a say."
    "A murmur rolls through the crowd—voices layering atop each other: older fishermen worrying about timelines; a youth organizer asking about job guarantees; a retired teacher asking who decides where the wall goes. The meeting is becoming a chorus of practical fear."
    "Marta leans in, insistence like a sharp scent."
    hide asha_moreno
    show marta_chen at right:
        zoom 0.7

    marta_chen "Pilots are endless unless there's teeth. If we pilot, we pilot with legal guardrails that protect property rights. We run sensors ourselves."
    "Eli's voice grows, warm and blunt."
    hide noah_reyes
    show eli_duarte at center:
        zoom 0.7

    eli_duarte "And if a wall means taking away the boatyard? You know what that does. You know what that erases."
    "Lila's PR lead flips a slide showing job numbers and reduced insurance rates. The graph is pretty. The promise is immediate safety for the highest number of people. It hums like a low beacon."

    menu:
        "Straighten the compass and speak from the ledger":
            "You set the compass against your palm like an anchor, clear your throat, and quote the cost-benefit numbers you prepared; the room quiets as the facts pull attention toward pragmatic terms."
        "Catch Noah's eye and speak from memory":
            "You let your gaze find Noah; together you recall a late tide when the whole neighborhood came out to push a leaking boat ashore. Your words turn toward shared memory, and faces in the crowd soften."

    menu:
        "Name a visible public safeguard — open data portal with community klaxon":
            "You propose a public portal that streams sensor data and triggers community alerts; neighbors nod, the proposal feels concrete and immediate."
        "Propose a staged pilot with strict community oversight":
            "You suggest a staged rollout: municipal buildings first, then residential trials with community monitors; the plan appeals to cautious minds in the crowd."

    menu:
        "Push the hybrid plan publicly, demanding local governance and sensor access.":
            jump chapter4
        "Openly propose pausing to pilot Lila's tech in a strictly monitored trial.":
            jump chapter7
        "Call for a private negotiation with Mayor Rosa and Lila to buy time.":
            jump chapter13
    return
