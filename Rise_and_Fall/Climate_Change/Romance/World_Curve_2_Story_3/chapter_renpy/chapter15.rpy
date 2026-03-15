label chapter15:

    # [Scene: Town Hall | Midday — Council Session]

    scene bg ch14_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady cello with a minor progression]
    # play sound "sfx_placeholder"  # [Sound: Muffled rain on the roof; distant murmurs from the gallery]
    "You stand at the lectern with the tablet balanced on both palms, the cautious report open but not an instrument of triumph. The air tastes like copper and wet paper — policy documents and the smoke"
    "of too many last-minute coffees. The room is warm in a way that makes your collar stick; the warmth feels political."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "We designed the trial to monitor a range of responses across the flats, with both living structures and engineered reinforcement. The data will guide adaptive management — not preordain one pathway."
    show aria_chen at right:
        zoom 0.7

    aria_chen "And the funding? The developers have committed to underwriting the monitoring phase, with an option to build contingent on the trial's 'validation.' That clause is a practical necessity given the economic fragility of the town."
    "You hear the word validate wrapped in a velvet glove. Validation can be neutral; validation can be a lever. You feel, like a cold tide, the pressure of ledger lines and job counts pressing against the maps you once folded in private."
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "Isla, if they reframe the monitoring as pilot validation for hard defenses, the flats will be boxed out. The reefs will be paved over. You promised we'd keep the community in the loop."

    isla_morgan "We wrote community engagement into the protocol. The monitoring is transparent."

    luca_moreno "Transparent when it's convenient. When it's not, it becomes a 'technicality.'"
    "The exchange ripples across the rows. Aria Chen's expression does not change; her hands fold like closed shutters."

    aria_chen "We move forward because we cannot let the town erode while we debate. My constituents need jobs. They need roofs that don't leak. There will be oversight."

    "Jonah Merrick (from the gallery)" "Oversight don't buy you a boat back when the mooring's gone."
    "A hush. Jonah's voice carries salt and the gravel of decades. The council is a place of balances; the harbor is a place of losses that measure the price."
    "You read the faces in the chamber — some hopeful, some resigned, many calculating their immediate bills. You know the science is not a neutral shield here; it is a tool placed into a contested handsaw."

    isla_morgan "We accept the joint trial terms with conditions. We insist on third-party audits and a binding clause to protect the salt flats' most sensitive corridors."

    aria_chen "We will honor those clauses. We will write them into the contract."
    "Her words are precise. You sign the amendment, not in triumph but in exhaustion, the tablet's screen reflecting a pale version of your face. The vote passes with a mixture of applause and quiet walks to the exits. The council's seal clicks; the developers smile."
    "You walk out of the chamber smelling of varnish and forced civility, and Luca's silence follows you like a stone."

    menu:
        "Let Aria make the public announcement while you step aside":
            "You stay in the lobby, wrists numb from the tablet, as Aria frames the trial as a compromise that saved jobs. Cameras flash, and the words 'guided the science' echo down the hall, thin as salt spray."
        "Step forward when Aria begins speaking and correct the language":
            "You interrupt, voice higher than you'd like. You insist on 'trial' not 'validation,' on 'pilot' not 'precedent.' Aria's smile tightens; a reporter angles a microphone. The room feels smaller."

    # --- merge ---
    "Narrative continues at the Salt Flats scene."
    # [Scene: Salt Flats | Early Morning — Construction Season]
    hide isla_morgan
    hide aria_chen
    hide luca_moreno

    scene bg ch14_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Low wind strings, a single piano motif]
    # play sound "sfx_placeholder"  # [Sound: Distant engines, the cough of diesel, gulls lashing out above the noise]
    "The living structures you designed climb from packing crates like awkward seedlings: woven mats seeded with oysters, strategically placed gabions. For a while, the mix looks hopeful — clusters of new life in measured intervals. The monitors hum softly, recording salinity, current vectors, fish counts."
    "Then the developer's engineers bring in machines that cut a straight line through your softer work. The clause you fought for — 'allowance for complementary hard works if pilot 'fails' thresholds' — is triggered on a"
    "metric you did not anticipate. The thresholds are technical, but the math collapses into policy: once erosion at a certain transect persisted for three sequential evaluations, the contract allowed reinforcements."
    "You stand at the edge of the work site and feel a grief that is tactile: the salt under your nails, the sting on your face when the wind whips the newly poured concrete's chemical smell."
    "The flats reflect the sky in small pools, and in those mirrors the horizon looks wrong."

    "Fisherman (off-screen)" "Those walls will keep the waves out — but they'll keep our nets empty, too."
    "You watch boats that once threaded the shallow channels now find their runs obstructed. Moorings that had been in families for generations are relocated or removed; some boats are hauled out and sold. The market stalls"
    "that used to bristle with the day’s catch thin over weeks into strangers hawking sleeves of imported fillet."
    "An engineer in a hi-vis vest approaches, clipboard in hand, rehearsed empathy in his face."

    "Engineer" "The mixed defense reduces risk for most town parcels. The economic modeling suggests resilience for residential zones and new job opportunities in construction."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "At what ecological cost? At what cost to those who fish the flats by hand?"

    "Engineer" "We believe the trade-offs are acceptable and temporary."
    "Acceptable. Temporary. Words that have been used to smooth outrages since the first harbor was paved."

    menu:
        "Attend the developers' ribbon-cutting to ensure a presence for the community":
            "You stand at the ribbon-cutting, hand hovering near scissors you eventually let someone else handle. Photographers flash; your name is printed in the program as 'guide to the trial.' A fisherman turns away when you try to meet his eye."
        "Refuse to attend and walk the flats alone instead":
            "You skip the ceremony. You walk mud and reeds, touch barnacled pilings, and count small losses—an old mooring ring, a child's toy boat half-buried. Your absence at the ceremony becomes a quiet broadcast of distance."

    # --- merge ---
    "Narrative continues at the Promenade scene."
    # [Scene: Promenade | Afternoon — Months Later]
    hide isla_morgan

    scene bg ch14_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: A deceptive upbeat rhythm undercut by minor key violins]
    # play sound "sfx_placeholder"  # [Sound: The slap of pamphlets, low chatter, a child's laughter that sounds distant]
    "You arrive to a public acknowledgment ceremony: plaques, speeches, a photo op for the paper. On the makeshift stage, Aria thanks you personally for 'guiding the science' that made the project politically and technically viable."
    show aria_chen at left:
        zoom 0.7

    aria_chen "Isla Morgan's careful work showed us how to move forward without losing Greyhaven. Her stewardship has been invaluable."
    "Applause. Your name in print. The honor glitters like salt on a fish's scale."
    "Luca Moreno slips through the crowd, expression folded into a shadow you know well."
    show luca_moreno at right:
        zoom 0.7

    luca_moreno "You handed them the fork, and they ate the heart."
    show isla_morgan at center:
        zoom 0.7

    isla_morgan "It wasn't like that. The trial gives us a way to monitor and adapt. We can still protect sensitive channels."

    luca_moreno "You can say 'monitor' until water runs clear, but decisions were written into the contract the day they signed. You lent them legitimacy, Isla. They needed a scientist to sell this as responsible."
    "His voice breaks on the last word. There's anger there, but underneath it is a deeper hurt — a sense of betrayal, not just of policy but of shared ideals."

    isla_morgan "I thought binding clauses would limit damage."

    luca_moreno "You thought. You didn't fight, Isla. You offered them terms and they bent them into cover."

    isla_morgan "Luca, I—"
    "Luca's mouth snaps shut. He turns away, eyes like flint. For a second you hope he'll stay, that he'll argue the nuance, that the two of you can stitch rage into strategy. Instead he walks to"
    "the edge of the promenade, pauses as if to look at the flats where the seabed has been rewritten, and then leaves without looking back."
    "You feel the leave like a hand gone from your wrist. It is not just Luca walking away; it is the easy possibility that companionship once promised."

    luca_moreno "Don't find me when you need someone to blame this on."
    "The crowd's applause is a thin sound. You are applauded for guidance; someone else paid in ways that smaller hands calculate differently."
    # [Scene: Greyhaven Hospital | Night — After the Storm]
    hide aria_chen
    hide luca_moreno
    hide isla_morgan

    scene bg ch14_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, each note slow and hollow]
    # play sound "sfx_placeholder"  # [Sound: The distant beeping of monitors; a cart's wheels creak]
    "The storm comes swift and without malice — just a mass of wind and rain. A commercial roof, weakened and unmaintained during the scramble after the early evacuation, collapses in a small neighborhood where Jonah checked"
    "on an old friend. You learn this by a nurse's soft knock and the way her eyes drop when she speaks."

    "Nurse" "He's been asking for you. He kept asking if you'd come."
    "You enter the room to find Jonah reduced to a silhouette under bright clinical light. His hands — those hands that had once mended nets — are folded on the blanket like folded years. Machines watch him like hesitant witnesses."
    show jonah_merrick at left:
        zoom 0.7

    jonah_merrick "You came."
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "I— I wasn't sure if you wanted me."

    jonah_merrick "You're the one who brings the numbers, Isla. I wanted to see if the numbers had grown a heart."
    "You sit, the chair creaking beneath you. The hospital smells of bleach and something else your memory can't name: the scent of impending absence."

    isla_morgan "They turned some of the flats into walls. The moorings… they took moorings. Jobs changed. Luca left."
    "Jonah Merrick's eyes crinkle in a smile that is almost a cough."

    jonah_merrick "Jobs? Everything's a job now, until it's not. You did what you could—don't make your head the harbor for every loss."

    isla_morgan "You don't get it. My science was used as a seal stamp. They say I guided the trial — I guided them into paving over a part of what keeps our fish coming."

    jonah_merrick "Science don't always keep boats afloat. People do. You paddled, girl. Sometimes the tide pulls the paddle away."
    "He reaches and takes your hand with surprising strength. His skin smells of tobacco and hospital lotion, the two mixing into a memory you will carry."

    jonah_merrick "Don't let 'they' write every history. Remember them loud enough that the stories don't die with the moorings."
    "He squeezes once. The monitors murmur. He is gone in a way that is small and absolute."
    "You sit with that smallness, and the room narrows to the space where Jonah's breath used to be and no one can push the tide back into place."
    # [Scene: Greyhaven Harbor | Dawn]
    hide jonah_merrick
    hide isla_morgan

    scene bg ch14_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Single cello line, low, unresolved]
    # play sound "sfx_placeholder"  # [Sound: The distant slap of water against engineered concrete; a lone gull]
    "You stand at the water's edge with the compass in your palm. The brass is warm from where it has nested against your skin all these years. You think of Jonah's hand in yours, of Luca's"
    "departure, of the applause, and of the ribbon-cutting photographs where you smiled like someone who had not bargained with loss."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "We saved roofs,' you tell the water. 'We saved walls."
    "You feel the sentence like a ledger balanced on a nail. It is true — rooftops no longer leak in the neighborhoods the wall shields. Children play on paved promenades without the damp clinging to their sneakers. There is relief. But it sits next to a quieter, grimmer account."
    "The flats are different now. The tidal flows are rerouted around concrete lips; the reed beds that used to catch the sun are narrower. You watch small fish circle where their paths used to be open, fewer in number, less reckless."
    "You think of the fishermen who lined up in the cold to tell you about lost nets, of Maya's eyes when she called to ask about work options in the new economy. You think of Jonah telling you to remember the stories loud enough."
    "There is an ache that is not sharp so much as persistent, a low tide of regret."

    isla_morgan "The town survives. It is not the same."
    "You tuck the compass back into your jacket. The metal is heavy in its smallness, a counterweight to the way decisions feel now — heavy, inescapable."
    "A child runs past, chasing a dog, oblivious to the line where the flats end and the seawall begins. The dog splashes in a shallow pool that used to be deeper. For a breath you watch and almost feel something like forgiveness in the ordinary motion."
    "Then the wind picks up, and the seawall answers it with a clean, indifferent slap. The town stands. It is intact in the ways that matter to ledgers and to insurance forms. But you know, in"
    "the neat smallness of certain losses — the mooring rings, the reed beds, the afternoon nets that no longer sing with fish — that the town has been altered in a way ledger lines will never"
    "fully count."
    "You look toward the promenade where lamp posts blink on as if in apology. You close your fingers around the compass and allow the salt air to taste like both relief and something you will carry"
    "for years: the knowledge that sometimes survival requires choosing among harms, and those choices do not come without a bill."
    "You let the compass rest against your sternum, and for a long moment you let the harbor be loud with what was bought and what was lost."
    hide isla_morgan

    scene bg ch14_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Cello continues, dropping to two notes that do not resolve]
    # play sound "sfx_placeholder"  # [Sound: Wind, then silence]

    scene bg ch14_601bcb_7 at full_bg
    "THE END"
    # [GAME END]
    return
