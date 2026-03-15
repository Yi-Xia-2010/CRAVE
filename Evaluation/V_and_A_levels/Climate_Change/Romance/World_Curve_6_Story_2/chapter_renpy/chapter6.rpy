label chapter6:

    # [Scene: Saltwood Dunes Nursery | Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Fragile, hopeful strings — bright but thin]
    # play sound "sfx_placeholder"  # [Sound: Soft laughter, the scrape of plastic trowels, distant gull calls]
    "Narration:"
    "You wake to the work you chose. The town's breath is here — in the rhythm of spades, in Nyla's clipped instructions over a tablet, in the cadence of Old Man Cala's voice leading the planting"
    "chant like a metronome of memory. For weeks the living dunes have been a kind of vindication: small ridges knit by root, swale by swale, a slow architecture of green. You taste salt and dirt together;"
    "it tastes like purpose."
    show maya_serrin at left:
        zoom 0.7

    maya_serrin "Okay, on three — dig low, press the roots in, tamp the crowns. Keep a meter between each plug; let the rhizomes do the rest."
    "Narration:"
    "You hear Aiden's boots slap the wet sand; he comes with the tide in his gait, hands still smelling of tar and fish. He doesn't parade belief — he shows up. That's enough."
    "Aiden Koa: (laughing) 'If this works, you'll be giving me an excuse to avoid the pier forever.'"

    maya_serrin "You can always come for the victories and leave before the council meetings."
    show aiden_koa at right:
        zoom 0.7

    aiden_koa "Deal. But only if you promise not to make me chair a volunteer rota."
    "Narration:"
    "He offers you a roll of burlap. His fingers are cold; you take it and feel the small trust in an exchange. Old Man Cala starts the chant again: a short, rough rhythm that the children"
    "mimic with reverent seriousness. Mayor Hale passes through, his smile practiced, his folder damp at the edges. The community hums in a way that feels close to salvation."

    menu:
        "Teach a child the planting chant":
            "You kneel, guide a small hand to the soil, let the chant wear into your throat. The child looks at you with a seriousness that makes your stomach twist in a good way."
        "Check the tide gauges with Nyla":
            "You stand, brush sand from your knees, and walk to Nyla’s station. The gauges hum; the numbers look normal — but your eyes don't stop hovering on the seasonal curve."

    # --- merge ---
    "Continue"
    # [Scene: Tide Research Station | Late Afternoon — Weeks Later]
    hide maya_serrin
    hide aiden_koa

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Underlying low pulse — steady, watchful]
    # play sound "sfx_placeholder"  # [Sound: The soft mechanical beeps of instruments, the distant slap of small waves]
    "Narration:"
    "For a while, the math and the ritual line up. The nursery plots become coherent ridges; gulls pilot smaller waves outward. Fisherboats sit at the quay with room to breathe. People who worried at the hall"
    "now pass on the shore and nod. There are photographs: kids with mud on their sleeves, Old Man Cala with a fistful of grass, you with your thumb over the tide-watch like a benediction."
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "You did good work. The council's still nervous about the budget, but—' (he shrugs) 'If we can show reduced risk at the southern crescent, that's leverage."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "Leverage for more community grants, not handing over control."
    "Mayor Jerome Hale: (careful) 'Of course. Control stays local.'"
    "Narration:"
    "You file his words into the same drawer you keep your worst anxieties; they close but sometimes stick. You and Aiden steal a quiet moment by the cliff, watching reefs of foam. He squeezes the space"
    "between your palm and the tide-watch and says nothing, and the silence thickens with things you both will not name aloud."

    menu:
        "Tell Aiden you still fear the models":
            "You find the words and lay them out. He listens, jaw working. He doesn't fix anything but he steadies you by holding your gaze."
        "Pretend you're fine and laugh":
            "You force a laugh around the edge of fear. He laughs too, but his eyes rain cracks you can't smooth."

    # --- merge ---
    "Continue"
    # [Scene: Saltwood Cliffs | Early Storm Season — Night]
    hide mayor_jerome_hale
    hide maya_serrin

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Low drums building into tense percussion; the tempo quickens]
    # play sound "sfx_placeholder"  # [Sound: Wind rising to a howl, boards creaking, the ocean a growing animal]
    "Narration:"
    "The season arrives like an accusation. The forecasts call for a larger-than-normal surge; volunteers stand with sandbags and wet-booted resolve. You coordinate, you reassign teams, you send messages to those with low-lying addresses. Nyla posts live visualizations on the community feed, pixels like small emergency lamps."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "The surge is stacking faster than the models showed. We need to evacuate the southern crescent now."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "Evacuation route A compromised — send the beach shuttles. Inform the quay. Old Man Cala, get people inland."
    "Old Man Cala: (gravelly) 'We move as one, child. We sing, we go. The tide cannot take what walks behind us.'"
    "Narration:"
    "The sound of the wind is a body moving around you. You taste metal and old rain; your palms are raw from tying knots. Aiden reaches for a rope, and when your fingers brush, electricity arcs — not tenderness but a bolt of shared alarm."
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "Maya — the boardwalk's already undercut. Boats are loose. We can't hold everyone if that surge wedges through the southern low."

    maya_serrin "Then we move people now. Push the children up to the hall. Mayor Hale, coordinate the shelter."
    "Mayor Jerome Hale: (voice breaking) 'We're calling for volunteers at the quay to secure small craft. We can't get everyone in one go—'"
    "Narration:"
    "You hear the implicit math in his sentence: not everyone will be first. Your chest clenches, breath thinning like a tide leaving too soon. You send two teams south, and then another, and then find yourself directing like a conductor of a shipwreck."
    # play sound "sfx_placeholder"  # [Sound: A sudden, metallic groan. The boardwalk shudders as a plank gives.]
    "Narration:"
    "Chaos blooms. The sound of splintering boards rips through the night. A pool of light reveals the boardwalk's edge as it collapses inward, sucked into a mouth of black water. A child's cry pierces the wind and you feel the world tilt."
    "Aiden Koa: (shouting) 'Push! Get the kids up! Move!'"
    "Maya Serrin: (yelling) 'Now! Now! Now!'"
    "Narration:"
    "Your lungs burn with the rawness of shouting. You sprint with others over half-submerged planks, gripping a slippery handrail that shakes beneath your weight. The tide finds the weakest seam — the southern crescent's old levee — and pulls like a patient hand unzipping the shore."
    # play music "music_placeholder"  # [Music: Percussion at full force; strings in dissonant clusters]
    # play sound "sfx_placeholder"  # [Sound: A sustained roar as water inundates the crescent]
    "Narration:"
    "You watch houses — not faceless structures but places with dishes drying on racks, with quilts, with someone's week's wages stacked in a drawer — tilt and go. The water shaves foundations away like an eraser."
    "Boats, half-sedate at rest, are torn like toys and tossed inland or into the breakers. The quay creaks and then parts. People scream and curse and pray; there is no order that can fully hold what"
    "the sea wants."
    "Old Man Cala: (hoarse) 'We did what we could. We are not gods.'"
    "Narration:"
    "You land on slick mud, your boots sinking. You taste salt and iron. Your thought fractures into tiny, precise shards — the nursery ridges held here and here, the school above the cliff intact, the southern row gone. The victory you had savored turns brittle in your mouth."
    # [Scene: Southern Crescent — Dawn After the Surge]
    hide nyla_torres
    hide maya_serrin
    hide aiden_koa

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano and wind — a hollow, aching motif]
    # play sound "sfx_placeholder"  # [Sound: Distant sobs, the scrape of mud under boots, sea sighing as if tired]
    "Narration:"
    "At first you move on automatic — cataloguing, searching, finding. Your notes are a litany of what remains and what does not. You know the names of almost everyone who lost a room, a roof, a"
    "boat. The southern crescent is a jagged seam where home and sea failed to negotiate."
    "Volunteer: (soft) 'They lost the Miller place. The Garcias. Old Mateo's shed—'"
    "Maya Serrin: (voice thin) 'Are they safe? People — are we accounting for everyone?'"

    "Volunteer" "Most are accounted for. Some were pulled in the nick—"
    "Narration:"
    "You stop hearing the accounting. Your feet carry you toward a row of cottages you remember as small, a line of familiar faces at markets and docks. Now they lean at impossible angles, windows like open"
    "mouths. The water has chewed the porches and dragged out furniture into a ruin-strewn tide."
    "Aiden Koa: (coming up beside you, voice low) 'Maya.'"
    "Narration:"
    "He looks like a map of grief. His jaw is clenched; his hands are raw from hauling and failing and holding. He places both hands on the warped doorframe of a fisher's house that has collapsed"
    "inward. He doesn't touch you at first. When he does, it is because of momentum — a leaning into the nearest solid person."
    show aiden_koa at left:
        zoom 0.7

    aiden_koa "We gave our all. We worked with what we had."
    "Maya Serrin: (internal) You want to say: it's not enough. You want to say: I should've taken Dr. Elena Park's offer; I should've found a way to stitch the concrete where it would have bought time."
    "But the words don't form cleanly. Responsibility is a burr that won't be plucked without tearing the skin."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "I know. I know we did everything we could."

    aiden_koa "Was that everything, Maya? Or was it what you wanted to be everything?"
    "Narration:"
    "His question lands like a stone thrown into a still pool, making concentric circles you can't stop. You search for an answer. You reach, instead, for explanation, for the scaffolding of reasons: ethics, autonomy, fear of"
    "ceding their coast to a corporation that would wall it off and change everything; the slow building of something living rather than a machine. They crash like fragile boats against the hard fact of the tide."
    "Mayor Jerome Hale: (coming up behind you both, voice grave) 'Some will call this a moral victory with a cost. Some will call it negligence. Right now, we have to be with the people.'"

    maya_serrin "We will be with them. We will rebuild. We will—"
    "Narration:"
    "Your voice fractures. The promise feels insufficient, a bandage pressed to a wound that keeps bleeding. Old Man Cala sits on a shifted stoop, salt beading in his beard like small, disrespectful stars."
    "Old Man Cala: (soft, final) 'You can hold a dune and lose a home. The sea doesn't judge our intentions. It takes.'"
    "Narration:"
    "You want to rage at the sea, to rage at the universe, to rage at yourself. Instead, you move through grief like a surgeon through tissue — careful, methodical, because there are still people who need hands."

    "Volunteer" "They're asking about aid. The shelter's full. We need more blankets."

    maya_serrin "Prioritize the elderly and injured. Get the boat teams to distribute food. Nyla — triage the requests on the feed; mark urgent."
    "Nyla Torres: (stiff) 'On it. We're pulling up what we can.'"
    "Narration:"
    "You command out of muscle memory. Every directive is a stitch. It keeps people breathing but it does not stitch the hole in you. The town survives; it is made of people pulled upright with hands that smell like wet wool and rope. But it is not intact."
    # [Scene: Quay — Midday, Aftermath]
    hide aiden_koa
    hide maya_serrin

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Mournful cello long notes, a wind that will not let up]
    # play sound "sfx_placeholder"  # [Sound: Quiet conversations like the scraping of broken shells; the occasional sob]
    "Narration:"
    "You stand in mud that tastes like wrong answers. You press your thumb to the tide-watch until the brass heats under your palm. The town's map of loss spreads like a bruise. Aiden stands next to"
    "you, and for the first time since the dunes sprouted, your hands search each other not for comfort but for an origin of blame. There is none to be found — only wet cold seeping between"
    "your fingers."
    "Aiden Koa: (voice barely a whisper) 'They lost their boats, Maya. That was their life.'"
    "Maya Serrin: (voice tight) 'We tried to protect the shore, not to rip their way of living from them.'"
    show aiden_koa at left:
        zoom 0.7

    aiden_koa "You refused what might have helped them because you feared what it would do to our identity. Did we save identity at the cost of people's homes?"
    "Narration:"
    "His words are a scalpel. You turn over every choice like a stone. You see the meetings, the chants, the laughter — and then the night the surge found a seam. You remember your refusal with"
    "increasing clarity: a cabinet meeting where you chose autonomy over outside steel, a signature withheld that might have channeled concrete where the dune could not reach. You feel the tug of your mother's house in your"
    "bones, the ballast of guilt set loose."
    "Maya Serrin: (internal) You are trained to look at systems, to prefer solutions that respect ecologies. You are also a daughter who watched a home drown. You thought your stubbornness would mean the town would not lose what you had. Instead, stubbornness held like a barge and then snapped."
    "Aiden Koa: (soft, hurt) 'I trusted you to keep us from being swallowed. I wanted you to be right.'"
    "Narration:"
    "There is no clean reconciliation. You find that common phrases — 'we did our best', 'we will rebuild', 'we are resilient' — slide off like water from oiled cloth. They do not cling to the ache"
    "in people's faces. Your empathy, the thing that made you fight with everything you had, now sits like an accusation: the same heart that pushed to protect habitat also kept out a tool that might have"
    "bought time."
    "Old Man Cala: (looking at both of you) 'You loved this place. Love is not innocent. It asks hard things.'"
    "Narration:"
    "He reaches for Aiden's hand with his own cracked palm. He looks at you and then away, eyes mourning both what was saved and what was taken."
    hide aiden_koa

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: The cello descends to a single, sustained note — unresolving]
    "Narration:"
    "You have preserved much: dunes that will, in time, soothe younger storms; neighborhoods inland that stand ready; a model other communities might watch, maybe even adopt. But in the southern crescent there are empty doorways that"
    "remember dinners and birthdays and the small liberalities of daily life. Victory tastes like ash because someone paid what you refused to buy."
    "Aiden Koa: (voice breaking) 'I don't know if I can forgive you for this. Maybe I don't want to.'"
    "Maya Serrin: (voice small) 'If you leave because of this—'"
    show aiden_koa at left:
        zoom 0.7

    aiden_koa "I'm not saying I'll leave. I'm saying right now there's a line. I need to know you see what happened."
    "Narration:"
    "You want to say: I see. You want to say: I am sorry. Those words are not enough. They are not currency for houses, for boats, for the shape of a life carved by tides. They hover in the space between you like smoke."
    "Mayor Jerome Hale: (stepping closer, voice low) 'People will need long-term support. We'll apply for federal aid and look for low-interest loans. The harbor commissions will need liaison — Dr. Elena Park may still have resources to offer, even now.'"
    "Maya Serrin: (reflex) 'I told her no. I can't—'"
    show mayor_jerome_hale at right:
        zoom 0.7

    mayor_jerome_hale "You told her no then. We have to do what helps now."
    "Narration:"
    "The idea of re-opening talks feels like turning a wheel you had welded shut. Pride, principle, and guilt twist together. You think of the choices ahead: rebuild living dunes and accept that some livelihoods are gone;"
    "accept engineered help and possibly give away jurisdiction; carve a hybrid path and risk being accused of hypocrisy. Each path tastes of ash in different ways."
    # [Scene: Saltwood Cliffs | Dusk — The Town Gathers]
    hide aiden_koa
    hide mayor_jerome_hale

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, elegiac harp over muted strings]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the occasional choked laugh; a gull wheel overhead, indifferent]
    "Narration:"
    "You stand at the edge of the crowd, the tide-watch an anchor in your fist. Old Man Cala begins a quiet chant not of victory but of grieving — a way to make meaning out of"
    "loss. People exchange blankets and stories; someone sets down a pot of coffee that has been shared until it is thin and bitter. Aiden stands near the door, his outline a silhouette against the dim hall."
    "He does not reach for you."
    "Old Man Cala: (softly) 'We tend what we can. We remember what we lose. Both are sacred.'"
    "Narration:"
    "You nod because there is no other thing to do that satisfies the liturgies of both science and love. The town will go on; it will rebuild in places; some things will never be the same."
    "You pressed your hands to the work you believed in, and the sea answered with its own calculus. The cost is counted in rooms emptied and in the softened look on Aiden's face."
    "Aiden Koa: (quiet, to you) 'I loved that you fought for the town, Maya. I loved that you wouldn't sell us out. But I loved my neighbors' boats too. I loved our way of living. I don't know how to hold both now.'"
    "Maya Serrin: (final, thin) 'I don't either.'"
    "Narration:"
    "The night condenses around that admission. It is not a resolution. It is not the sweeping reconciliation the heart wants. It is a small, gaping honesty that may or may not be enough to keep people close through repair and time."

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: The music fades into a single, sorrowful chord]
    # play sound "sfx_placeholder"  # [Sound: The ocean exhales]
    "Narration:"
    "You stand in the mud, salt-streaked, stomach hollow like a boat's hull. You have preserved something essential in the landscape, but the cost is carved into the town's living memory. The dunes will hold future storms;"
    "the southern crescent will hold ghosts. Your empathy saved much and, by the same gesture, failed some. The victory is ash. The town survives. You survive, but both of you carry scars that will sing whenever"
    "a tide-watch ticks."

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Single sustained note until silence]
    "Narration:"
    "You think of your mother’s house, of all the small domestic debts you swore never to let happen again. You think of Aiden's face and the way hope and blame braided together between you. You think"
    "of Old Man Cala's chant and Nyla's tired grin. The moral calculus you made still stands; it produced both shelter and ruin. There is no clean absolution."

    scene bg ch6_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
