label chapter5:

    # [Scene: Ferryworks Greenhouse | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hiss of a welding torch, the soft thud of booted footsteps on the steel deck, a low hum of generators]
    # play music "music_placeholder"  # [Music: Fast, buoyant strings—hope in motion]
    "You walk in on the noise of a place already deciding what it wants to be. The Ferryworks smells of wet soil and hot metal: rich loam under a layer of solder fumes, the clean bite"
    "of salt on the air. Your notebook is folded into the inside pocket of your jacket, thumbed margins pressed soft by every meeting and scrawl. The small spark from Chapter Four still lives under your ribs"
    "— that ember of agreement with Calder Voss, the pact you made with hazard and people both."
    "Ori Navarro is at the aft bench, shoulders bent into a winged planter half-sculpted from a salvaged hull plate. His topknot is tight, cheeks flecked with paint; the welding goggles sit on his head like a"
    "crown. He taps the edge of the metal with the flat of his palm and grins when he sees you."
    show ori_navarro at left:
        zoom 0.7

    ori_navarro "Look at it — doesn't it want to fly?"
    "You let yourself smile because the thing is beautiful: curved, practical, and stubborn — the exact thing you love about his projects. Around him, Silas Roe moves like a practiced shadow, quick hands binding algae filters"
    "to a frame that will breathe with the tide. Old Mara sits on a milk crate in the corner, her voice a low hum you didn't realize you needed until it steadied you."
    "Old Mara: (softly) 'Tide remembers. Tide forgives. We will learn to move with her.'"
    hide ori_navarro

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The recorder light on Jun's collar blinks; a kettle on a smaller bench sings]
    "You move like someone mid-countdown, assigning volunteers, double-checking the battery matrix under a row of seedlings, sketching the final sensor array with the quick economy of someone who's learned to be exact where there's no margin for waste."
    "Maya Lin appears with a rolled set of legal drafts and a thermos. Her eyes are bright, ledger-face on, already speaking in short, efficient bursts."
    show maya_lin at left:
        zoom 0.7

    maya_lin "Volunteer shifts up two hours. Ferryback will need extra hands for the heavier blocks. Also —' (she taps a page) '— Jun says he has something for you."
    "Jun Park steps forward, reluctant smile softened by the warm light. He hands you a slim packet whose top sheet has been redacted: thick black bars, the legal printer's silence where meaning should be. You take it with fingertips that are damp from the garden."
    show jun_park at right:
        zoom 0.7

    jun_park "I scrubbed it for the meeting, but there are lines they didn't want the room to see yet. I thought you should read it before any cameras or speeches."
    "You peel back the legalese. The prototype is singing to you from the benches — the mangrove cuttings are rooting, tiny pale hairs like new constellations; the sensors on the outer planter ping, numbers flattening into"
    "a calmer line. Volunteers laugh on the deck when a test pump hissed and then steadied; a child squeals when water runs clear through a filter. That success pulls your chest forward, a rising tide of"
    "something like triumph."
    # play music "music_placeholder"  # [Music: A higher, quicker motif—anticipation twined with momentum]
    "But the redacted addendum catches at the edges of the moment. You read the scanned passage over and over — the letters remain, but clauses have been blacked out like tide marks. One line you can"
    "still see mentions 'relocation clause' and 'safety thresholds' with the neat cruelty of corporate phrasing. The more you read, the more the chord of joy in your chest hardens into something brittle and small."
    "Your hope refuses to break. Instead it tightens into a knot you recognize as focus."
    "Ori Navarro notices the change before you speak. He sets down his tool and comes close, wiping his hands on a rag with the reflexive intimacy of someone who builds things to soothe the world."
    show ori_navarro at center:
        zoom 0.7

    ori_navarro "You look like you swallowed a storm."
    hide maya_lin
    show ava_maren at left:
        zoom 0.7

    ava_maren "Jun handed me an addendum. It mentions a relocation clause."
    "Jun Park: (quick, pragmatic) 'It's redacted in parts. The thresholds are intentionally vague — they can be set after the pilot starts. It's better to be cautious about how that could be used.'"
    hide jun_park
    show maya_lin at right:
        zoom 0.7

    maya_lin "Then we tighten the language now. No ambiguity. Tenure guarantees — clear triggers, community oversight. We don't sign until it's explicit."
    "Ori Navarro reacts, both hands out, as if to hold the air between legalese and living things."

    ori_navarro "Or we push forward with the demo and make it irrefutable. Let the pilot be proof — public eyes, photos, people touching the wall. Once it's built, they can't displace what already works."
    "Your chest is a drumbeat: the Ferryworks hums with activity; the prototype hums with living roots; Calder Voss's cameras—eyes from the corporate side—are angled to show smiles and strong hands. The pilot's public optics are gold."
    "Your mind runs a hundred small calculations at once: resources arriving, pressure easing, but a clause like that could be flipped into a means of eviction later. There is no easy arithmetic that makes all harm"
    "vanish."

    menu:
        "Encourage Ori to build the annex now — make the pilot undeniable":
            "You nod, voice quick. 'Okay. Make it unignorable.' Ori's grin goes wide; he slaps the metal like it's a promise. The team rallies, energy spooling outward as more hands come to lift and weld. For a heartbeat the Ferryworks is all motion and incandescent possibility."
        "Insist we nail the legal language first — no signatures without ironclad tenure":
            "You fold the packet closed with a deliberate snap. 'We can't build what we can't stay by,' you say. Maya breathes out, relief and new work rewriting across her jaw. The room cools into carefulness, volunteers glance at Jun and the papers, and the day shifts from momentum to negotiation."

    menu:
        "Confront Calder Voss's representatives now — demand clause removal in person":
            "You grab the packet, your voice a tether. 'Bring them here,' you say. The announcement ripples through the Ferryworks; volunteers straighten. Calder Voss's team looks surprised but alert. It's an escalation; it's public; it forces a face-to-face that could cut the clause or fracture the deal."
        "Call Maya and Jun into a closed room to redline the clause before any more public exposure":
            "You map a quick path to the small meeting room, fingers already reaching for a pen. Maya's relief is immediate; Jun nods into his recorder and then switches it off. The Ferryworks breathes in, contracting into a focused, legal heart where words will be made to hold people."

    menu:
        "Accept a negotiated pilot with limited amendments—get it built fast.":
            jump chapter6
        "Refuse until community control clauses are ironclad—push for strict protections.":
            jump chapter6
        "Delay public partnership—keep scaling the prototype independently.":
            jump chapter14
    return
