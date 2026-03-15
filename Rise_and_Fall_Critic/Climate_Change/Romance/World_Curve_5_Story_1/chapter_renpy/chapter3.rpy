label chapter3:

    # [Scene: City Hall Hearing Room | Mid-Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain steady on the plaza outside, a low murmur of gathered townspeople, the dull clink of a ceramic mug against a saucer.]
    "You arrive carrying the momentum from the greenhouse — the crate emptied, the speech practiced, the seedlings promised. The echo of Asha's tablet, Cassian Rhys's mural glyphs, Ruben's slow smile still ride your ribs like tidewater."
    "The plan you left the lab with settles into your shoulders: facts, faces, a hope you can translate into policy."

    scene bg ch3_98c6f2_2 at full_bg
    # play music "music_placeholder"  # [Music: Soft piano motif, hopeful and steady under the murmur.]
    "The hearing room smells of too-cold coffee and rain-sheened paper. Seats are occupied by people with canvases of worry—anxious hands wringing scarves, children lulled by the gravity of grown voices. Mayor Lin Park sits at the"
    "center table, her scarf folded with practiced composure. A modest placard reads 'Town Forum: Coastal Plan.' Jonah Hale stands at the podium across from you, raincoat still beaded with water. His hair is neatly swept back;"
    "his slate-blue eyes assess the room like an engineer appraising a blueprint."
    "Cassian Rhys slides into the front row, the braided bracelet on his wrist catching the strip light. His smile is stubborn and small; a private vow, not a spectacle. Ruben is here — heavier with salt"
    "and memory — his cane tapping a patient rhythm. Nadia clutches a paper envelope; you know at once it's the school letter she promised to bring."
    "You inhale. The air tastes faintly of brine and recycled building heat. Your throat tightens — not with fear, but with the shape of responsibility. This is the public moment: your data and their stories must"
    "translate into something that counts in the Mayor's ledger and in the quiet lists people hold in their heads."

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone feedback, the soft clearing of throats.]
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "Thank you all for coming. We'll begin with community testimony, followed by presentations from both sides. Ms. Kestrel, when you're ready."
    "You step to the microphone. The strip light discovers the small tremor you didn't expect in your fingers and you tuck it into the cadence of your voice."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Good morning. I'm Mira Kestrel, Tidelab lead. We ran fourteen months of marsh attenuation trials along the Northpoint spit. The sensors show a median reduction in nearshore wave energy by twenty-five percent in moderate storm events, and a measurable increase in sediment accretion rates where cordgrass and oyster clusters were established."
    "(You pause to let the numbers settle like stones thrown into listening faces.)"

    mira_kestrel "Translated to livelihoods, that attenuation models as fewer overtopping incidents across the board and a thirty-eight percent reduction in emergency repair hours for households in the pilot quadrant. That—' (you flip to the marked page) '—is time, labor, and money households can keep. That's resilience that grows with the community."
    hide mayor_lin_park
    hide mira_kestrel

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft, involuntary murmur; someone murmurs 'that's something'.]
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "Those are compelling figures. Can you speak to scalability? And to the timeframe — citizens want to know when they'll see protection."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Scalability is iterative. We pair nature-based cells with modest engineered anchors to protect critical infrastructure initially, then allow ecological processes to extend protection outward. The pilot shows meaningful results within two seasons for neighborhoods with maintained stewardship. It does require steady community labor and adaptive management."
    show jonah_hale at center:
        zoom 0.7

    jonah_hale "Mayor, if I may. Iterative is not the same as immediate. Our consortium's barrier offers measurable, near-term security — designed to meet a thirty-year standard with funds already allocated. It buys time and makes the town marketable for long-term investment."
    hide mayor_lin_park
    hide mira_kestrel
    hide jonah_hale

    scene bg ch3_98c6f2_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A murmur of agreement from a few faces; a few frowns from others.]
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "We are not arguing for ideology over safety. We offer certainty. The barrier is tested. It is funded."
    "You hear the appeal of certainty. You also hear the price tags: displacement, altered shorelines, cultural cost. Your failed pilot — the one that took a season of miscalculated plantings and an unexpected storm — coils"
    "like a low ache behind your ribs. You remember the seed trays lost and the embarrassed apologies you made in front of neighbours. That memory makes your voice smaller sometimes; it makes you measure words with"
    "extra care."

    menu:
        "Smooth the tidewatcher pendant, breathe slow":
            "You tuck the tidewatcher under your collar, a small ritual that steadies the rhythm of your breath; the motion is private, but it steadies your voice."
        "Glance at Cassian, search for a familiar spark":
            "You glance toward Cassian Rhys. He meets your eye and lifts his chin minutely — an anchoring look. The heat behind your ribs eases by a fraction."

    # --- merge ---
    "The narrative continues."
    "You continue, buoyed by the quiet of a team that has your back."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We are not naive about scale or time. A hybrid approach leverages both community-driven marsh systems and targeted reinforcements. It keeps people local while managing risk. It—' (you look at Nadia, and the envelope in her lap) '—keeps school programs running, keeps elders in place who raised their kids here. It isn't perfect, but it grows protective infrastructure and jobs in tandem."

    "Nadia Hale" "Mayor — my class wrote to ask if they'll still be able to plant the orchard this spring. Those trees mean everything to some of us. Please don't let them become a story we only read."
    hide jonah_hale
    hide mira_kestrel

    scene bg ch3_98c6f2_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet sniffing; a few wet eyes.]

    "Ruben Hale" "I've fished these waters since before most of you were born. Trees move with the tide; roots find new ground. But when heavy walls go in place, the flow changes — and so do the places where fish come and where shells set. We need to make sure our fixes don't kill the rest of what keeps us fed."
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Mr. Hale raises an important ecological feedback that engineering should account for. Our designs include flush systems and spillways — engineered solutions for dynamic shores."
    "(Your reaction is instant, a scientist and a daughter of the bay both speaking at once.)"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Those systems can mitigate impacts but they also introduce maintenance dependencies, long-term costs, and governance issues we have to plan for with community oversight. The model we propose keeps control local as much as possible."
    show mayor_lin_park at center:
        zoom 0.7

    mayor_lin_park "This is where things are complex. The consortium brings funding and certainty; your team brings stewardship and lower long-term ecological risk but slower initial gains. The council is split. I want a solution that protects lives and livelihoods without hollowing out the town's soul."
    # play music "music_placeholder"  # [Music: Piano lifts into a warmer, ascending phrase; hope threads through the tension.]
    hide jonah_hale
    hide mira_kestrel
    hide mayor_lin_park

    scene bg ch3_98c6f2_7 at full_bg
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Ms. Kestrel, would you accept a public negotiation? A table where we outline phased reinforcements paired with your marsh scaling? It would be a hybrid plan with immediate anchors and a commitment to fund the living systems through the consortium's stewardship arm."
    "Mira Kestrel: (your mouth forms the question before your head does) 'And oversight? Community veto? Transparency on contracts?'"

    jonah_hale "A third-party audit, a public timeline, and community seats on the oversight board. We can draft terms to protect neighborhoods from eminent acquisition."
    "(He speaks like a man offering a blueprint. The offer is precise. It is also tempting.)"

    menu:
        "Nod slowly, signal willingness to negotiate aloud":
            "You nod and fold your hands on the lectern, willing to be the face at the table if it means the town keeps a say. The room exhales; it feels like opening a door."
        "Tighten your jaw, ask for stronger guarantees first":
            "You tighten your jaw and press for stronger, legally binding community safeguards before you agree to sit at any table. The room goes quieter; some faces look relieved, some wary."

    # --- merge ---
    "The narrative continues."
    "Cassian Rhys leans forward from the front row, whispering just loud enough for you, 'If you can keep them honest, you can keep us safe.' There's no drama in it — only practical faith."
    show mayor_lin_park at right:
        zoom 0.7

    mayor_lin_park "I'm proposing we do three things: one, schedule a public negotiation session with both parties present; two, authorize a city-sanctioned pilot with defined metrics, and three, allow community contingency measures in the draft. Ms. Kestrel — your leadership in a public negotiation would carry weight. Mr. Hale — will the consortium commit to a transparent, time-bound oversight structure?"

    jonah_hale "We will commit to a transparent structure, with benchmarks and external audits. If the hybrid model proves effective, we'll phase construction accordingly. If not, we keep the option open for more robust measures."
    "You hear the offer is a hinge. It gives you access to the negotiation table — influence you could wield — but also the possibility of being softened at the edges by political compromise. It offers"
    "the chance to preserve more than it risks. You think of the seedlings in Tidelab, of Ruben's slow nod, of Nadia's envelope, of Cassian Rhys's quiet promise. The weight of your past failure tugs again, reminding"
    "you that being at a table doesn't guarantee the community is heard in the room where money is counted."
    "The microphone hums, and the room narrows into choices. Mayor Lin's expectation hangs in the lit air like a tide line waiting to be crossed."
    "You can feel the ascent: community momentum, measured hope, new agreements on the table. The split will define which path that ascent takes."
    hide jonah_hale
    hide mayor_lin_park

    scene bg ch3_98c6f2_8 at full_bg
    # play music "music_placeholder"  # [Music: The hopeful piano holds.]
    "You prepare to answer — to decide how you will move forward for the town, for those you love, and for the living shore that raised you."

    menu:
        "Negotiate publicly with Jonah for a scaled hybrid plan.":
            jump chapter4
        "Form an organized grassroots blockade and public campaign with Cassian.":
            jump chapter7
        "Propose a city-sanctioned pilot that forces a transparent evaluation under Mayor Lin.":
            jump chapter10
    return
