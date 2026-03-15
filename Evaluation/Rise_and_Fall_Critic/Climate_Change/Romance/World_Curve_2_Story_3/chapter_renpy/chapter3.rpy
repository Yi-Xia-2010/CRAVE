label chapter3:

    # [Scene: Town Hall | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur of voices, the hum of Lina Park's recorder, a camera shutter like a heartbeat; distant, the sea keeps time with a slow, impatient hiss.]
    # play music "music_placeholder"  # [Music: Sparse strings; a low, descending cello figure underpins the air.]
    "You step into the room carrying the weather on your skin. The damp of the boardwalk clings to the cuffs of your jacket; the scent of sea and rain‑waxed wood sits behind the more immediate smell"
    "— sanitizer and coffee, the grown-up antiseptic of politics. Ivy's fingers find yours in the third row and squeeze, quick and steady. The pressure is the only language you can afford right now."
    "You feel the brass compass against your sternum. It is warm, like a small, private pulse — a reminder that direction matters even if the map is torn."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cassian's voice, polished and leveled.]
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "Havenport deserves certainty. Our engineers can deliver reinforced barriers within three seasonal cycles. Tideguard's model minimizes displacement and maximizes protection. The math is clear: large structures, monitored systems, immediate stabilization."
    "You follow his cadence, tasting the numbers as if they were a cold metal you cannot warm. There's a clean certainty to his sentences — a clinical comfort that bangs like a hammer on an already splintered floor."
    "Lina leans forward, recorder between her fingers."
    show lina_park at right:
        zoom 0.7

    lina_park "And what about access? Small fishers, community slips — how do you account for cultural access points in that model?"

    cassian_rhee "We can integrate access corridors, community docks — under contract. Our public‑private partnership model budgets for relocation stipends, job training. We are offering the tools for long-term viability."
    "You hear the subtext between the lines: under contract. Stipends. Relocation. The words settle in your mouth like salt."
    "Elder Tomas’s voice comes out low and rough, like driftwood."
    show elder_tomas_hale at center:
        zoom 0.7

    elder_tomas_hale "We don't want a wall that takes our harbor and our names with it. The sea here holds memories. You build a thing and you change the story."

    cassian_rhee "I respect memory, Tomas. We are not blind to heritage. We design with input — but we must act decisively. Hesitation costs lives."
    "Ivy squeezes your hand again. The gesture is small and all the clearer for it."
    "A sudden clack — airtight optimism: Ariana rises, hair clipped back, camera bobbing at her hip like a little drum."
    hide cassian_rhee
    hide lina_park
    hide elder_tomas_hale

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Her voice — bright, quick, slightly breathless.]
    show ariana_voss at left:
        zoom 0.7

    ariana_voss "We can scale nature-based engineering. If we pilot living seawalls along the most vulnerable stretch — combined kelp nurseries that attenuate wave energy and biofabricated anchors — we get protection that restores habitat. It takes longer, but it keeps people on their land and keeps the harbor alive."
    "She talks like someone telling you that a bruise can be healed without scraping the skin away. Her optimism is not ignorance; you know that. You also know how long 'longer' can be when a storm is a calendar away."
    show lina_park at right:
        zoom 0.7

    lina_park "Funding? Metrics? How do you guarantee performance against a major event?"

    ariana_voss "We'll pair community labor with Tideguard's sensors and independent verification. Transparency will be baked in: open dashboards, staged milestones judged by the council and local elders."
    show cassian_rhee at center:
        zoom 0.7

    cassian_rhee "With respect, those are pilot promises. Pilots do not stop a storm. What happens if you’re wrong at the wrong moment?"

    ariana_voss "Then we fail with our eyes open — but we don't hand over the town in exchange for fast security that might erase the pieces we came back for."
    "The room tightens. Someone coughs. A camera clicks; Lina's recorder hums like a live animal. You can see the calculus on people's faces: risk versus identity, speed versus stewardship."
    "You open your mouth once, to say something careful, something stitched from both data and memory, but the mayor's hand lifts."

    "Mayor" "Marin, the council expects a stance from the community leadership. We can't stall this vote forever. What should Havenport do?"
    "The question lands like a storm-door slamming. Eyes turn."
    "Ivy's hand is still in yours, anchor and accusation at once. Ariana's blue-streaked hair frames a face you want to shelter and that you also want to follow into the light. Cassian's posture promises the cool"
    "safety of certainty. Elder Tomas watches you as if he's waiting to see whether the town will remember itself."
    "You feel the compass again—warm—then hot, as if the metal remembers all the directions you did not take."

    menu:
        "Clear the throat and start with the data":
            "You push your voice forward, the words measured: 'We need to think in phases, with verification...' The room leans in to the careful plan you could recite by rote."
        "Speak from the heart — invoke the harbor's memory":
            "You let formality fall away. 'This harbor remembers our names,' you say. The room goes quiet; some faces soften, others tighten."

    # --- merge ---
    "The narrative continues with the mayor pressing for a public stance."
    "You feel the aftershock of that small decision before you've even chosen. The way you open affects the room's hunger for numbers or story. You sense Ariana's fingers curl around the strap of her camera; she looks at you as if you might braid the two into one answer."
    "Lina presses, voice sharp with professional hunger."

    lina_park "Marin — the town listens to you. You can tone the debate away from binaries. What's your position?"
    "Your mind catalogs: seedlings at the nursery, Elder Tomas's maps, the boathouse with its lamp throwing a honeyed circle on the floor — all of it balanced against Tideguard's contracts and polished solutions. Fear and responsibility thrum inside your ribs like a second, more insistent heartbeat."

    cassian_rhee "If Havenport vacillates, we lose leverage. We need a clear yes or no. Markets don't wait on nuance."

    "Ariana Voss (under her breath, not quite to you)" "You don't have to be all of us at once, Marin."

    menu:
        "Squeeze Ariana's hand back, quietly":
            "You return the contact — a small, private pact. Her eyes lift, steadier; she mouths 'thank you' without sound."
        "Keep your hands folded in your lap":
            "You tuck your fingers together, a deliberate smallness. Ariana's face flickers — disappointment, then resolve — and she straightens as if to stand without the touch."

    # --- merge ---
    "The room reacts and settles; the discussion tightens toward a public decision."
    "The room breathes. You can feel everyone's expectations as a physical weight: the council members with their ruled sheets, Lina's recorder, Tomas's carved walking stick leaned within reach. Outside, the sky finally, finally lets part of"
    "the storm announce itself — a sudden gust flings a rain-swept smell through the open transom."
    "Your inner monologue narrows, relentless and exacting. There's a set of futures branching from the shape of your answer:"
    "- Stand and refuse corporate barriers: a public resistance that galvanizes locals — loud, messy, risky."
    "- Negotiate privately: a shadow path that could secure protections without public rupture but asks you to trust quiet promises."
    "- Prioritize Ariana's living-seawall pilot and delay approval: buy time for nature-based proof, but risk losing investor patience and immediate defenses."
    "You can hear the tide in each option: the sound of cheering, the hush of closed-door deals, the low bend of patient work. Each would change what protection looks like and who gets to define it. Each will leave marks."
    "Your mouth opens. The mayor's face is intent, the room like a held breath. You feel the weight of Ivy's certainty and Tomas's memory. You feel Ariana's hope and Cassian's pressure. The compass at your throat"
    "is an ember. You realize choices will not only decide the town's infrastructure — they will decide whether the harbor is named in the future as memory or as a line on a contract."
    "Mayor: (soft, absolute) 'What should Havenport do?'"
    "You know, in the naked shape of the moment, that the answer will bind love, science, and the town's future into policy or into protest. You also know that whatever you say will carry consequences that will not unring."
    hide ariana_voss
    hide lina_park
    hide cassian_rhee

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The recorder's hum, the distant slap of rain against the window; cello notes drop like loose stones.]
    "You take in the faces one last time — Ivy's steady, Lina's hungry, Tomas's remembering, Ariana's hopeful, Cassian's measuring — and then you speak."
    "You do not finish. The sentence stops, breath caught at the hinge of the town's next long season."

    menu:
        "We refuse the corporate barriers; we lead community adaptation.":
            jump chapter4
        "I will negotiate with Tideguard privately to secure protections.":
            jump chapter7
        "We prioritize Ariana’s living-seawall pilot and delay final approval.":
            jump chapter10
    return
