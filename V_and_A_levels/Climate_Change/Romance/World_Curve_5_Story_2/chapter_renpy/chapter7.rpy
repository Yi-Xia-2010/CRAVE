label chapter7:

    # [Scene: Town Hall Meeting Room | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Pulsing low strings, insistent tempo]
    # play sound "sfx_placeholder"  # [Sound: Muffled gull cries from outside; the undercurrent of many conversations]
    "You start here because you chose to buy time—Conditional Agreement, Option B. The air tastes metallic and rain-heavy, as if the sea itself is listening. Mayor Ana's welcome is quick and practiced; the room leans on"
    "it like a brace. You remember the rooftop's expectant chord and carry its weight into this narrower, brighter space."
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "We need money in the ground and hands on the mud before the next season. This—this infusion—buys us that. Marin, you recommended it."
    "Her eyes find yours and, for a half-second, you feel the town's ledger laid across your chest. You keep your hands where they can be seen—flat against the table, fingers worrying the rim of your notebook"
    "beneath your palm. Your throat is dry with the kind of pressure that isn't sudden; it's accumulated, tidal."
    show marin_sol at right:
        zoom 0.7

    marin_sol "Conditional means oversight. Joint timelines. Independent sensors. No unilateral construction."

    mayor_ana_beltran "Agreed. The council will sign it. We can’t stall while the next high tide is counting days."
    "Jun Park shifts in his seat, handheld comm dimly reflecting on his palm. Relief moves over his expression like surf: quick, almost guilty. You notice it and the sight is a prick — you are not alone in weighing risk and relief."
    show jun_park at center:
        zoom 0.7

    jun_park "This gives us resources to pilot Marin's approach and TideLine's modules together. We can run parallel metrics."
    hide mayor_ana_beltran
    show aria_chen at left:
        zoom 0.7

    aria_chen "That is the plan. TideLine's platforms are modular—temporary by design. They reduce immediate risk while your marshes establish. Joint oversight reduces friction."
    "Aria's words are a well-cut set of tools: efficient, glossy. Her storm-gray suit seems to absorb the light and reflect order. There is a steadiness to her voice that attempts to compress worry into procedure. But"
    "where she offers certainty, your chest tightens with a different calculation: the fine balance between speed and sovereignty."
    # [Scene: TideLine Field Office | Early Evening]
    hide marin_sol
    hide jun_park
    hide aria_chen

    scene bg ch7_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Higher tempo, urgent synths]
    # play sound "sfx_placeholder"  # [Sound: The low hum of a server, footsteps on polished floor]
    "You follow Aria into a room that smells faintly of ozone and printer ink. Jun trails behind, checking a tablet. Dr. Lian sets up a sensor display on the table: a small constellation of live readouts—salinity, substrate compaction, tidal scour—numbers you can feel as if they press on your palms."
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "If we place our sensors here and here, the data overlays will show how the marsh and platform interact. We can calibrate in real time."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We need transparent data access. Community reviewers. Timestamped deployment logs."
    show aria_chen at center:
        zoom 0.7

    aria_chen "TideLine proposes a memorandum of understanding. Joint oversight committee—equal representation from the co-op and TideLine. Shared dashboards. Temporary deployment schedules."
    "You listen as lawyers translate promises into clauses. You thumb the edge of the MOU where a line reads 'temporary' and 'modular' in the same sentence as 'company-operated maintenance.' The words feel slippery."

    aria_chen "Sign here for the memorandum. It allows procurement to start immediately while oversight structures are formalized."

    marin_sol "I want the oversight language explicit around—"

    aria_chen "We included escrowed funding, Marin. We included a joint audit after six months. Your team will have full sensor access."
    "Her interruption is not rude; it is practiced. It places urgency in front of hesitation. The room leans forward—a dozen practical faces, the co-op representative, Mayor Ana—and the pulse in your neck quickens. The urgency is"
    "real: platforms in place sooner mean boats might be safe through one more season. The cost is the stretch of a contract where definitions can hide."

    menu:
        "Ask to read the indemnity section aloud":
            "You clear your throat and begin reading the indemnity clause into the quiet room; eyes move toward the paragraph where legal language nests intentions. Aria's jaw is paper-smooth. Jun's hand goes white around his tablet."
        "Trust the joint oversight promise and sign":
            "You place your pen on the dotted line and sign with a hand that trembles, convincing yourself of the urgency. The ink catches the light like a small compromise. Kaito's frown, later on the pier, will register it."

    # --- merge ---
    "The memorandum is signed with the clink of pens and the low, professional murmur of relief. For a sliver of a moment, it feels like a bridge: money, scaffolding, and a roomful of people committed to doing the hard, slow work right beside faster hands."
    "You pick one of those small acts and the sound of the pen is louder than it should be. The memorandum is signed with the clink of pens and the low, professional murmur of relief. For"
    "a sliver of a moment, it feels like a bridge: money, scaffolding, and a roomful of people committed to doing the hard, slow work right beside faster hands."
    # [Scene: The Old Pier & Fishing Co-op | Dusk]
    hide dr_lian_obasi
    hide marin_sol
    hide aria_chen

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: A taut, single guitar line — unresolved]
    # play sound "sfx_placeholder"  # [Sound: The creaking of pylons, distant mechanical beeps from TideLine equipment being loaded]
    "You step back onto the pier with your notebook under your arm. The town's reaction rolls in, uneven and immediate. Kaito stands with his arms crossed, rubber-soled deck shoes scuffing the planks like punctuation. Old Tomas"
    "leans on the rail, the ocean in his face, deliberation carved in the slow movements of his fingers."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You signed it. You said you'd be careful. That's a lot of power to hand over, Marin."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We didn't hand it over. We negotiated joint oversight, Kaito. We keep community representation on the committee."

    kaito_navarro "Joint oversight is a pleasant phrase. When something needs fixing at three in the morning, whose phone gets called? Their contractor list or our boys with rope and lanterns?"
    "Kaito's voice is low but fierce. He speaks for the section of the co-op that remembers long nights hauling nets through gusts and for the cultural ritual of the sea as community commons. The words land"
    "as pressure against your ribs—each syllable a reminder of what could be lost for a promise of speed."
    show old_tomas at center:
        zoom 0.7

    old_tomas "Are our tides being leased now? Are our nets collateral for their platforms?"

    marin_sol "No. The timeline ties maintenance back to the co-op's access. The MOU specifies temporary platforms and a withdrawal clause."

    old_tomas "Words and seals. The ocean remembers who cut its edges."
    "He looks at you in a way that is neither warm nor cold — complex and patient. His question is not a demand for specifics; it is a test: can you carry the town's story without letting it be rewritten quietly?"
    hide kaito_navarro
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "The sensors will show interaction. If the marsh loses function, we pause deployment. Data is our lever."
    hide marin_sol
    show kaito_navarro at right:
        zoom 0.7

    kaito_navarro "And if the lever is welded to a clause we didn't sign for? That's what I'm afraid of."
    hide old_tomas
    show marin_sol at center:
        zoom 0.7

    marin_sol "Then we pull the lever. We make the data public. We bring in auditors if needed."
    "Your voice locks into a rhythm with Lian's technical steadiness and Kaito's blunt protectiveness. It feels like triangulating a position in storm-bright coordinates: urgency, caution, and stubborn hope."

    menu:
        "Place a sensor at the mothballed net hut":
            "You gesture to Lian; she nods and extracts a compact sensor from her bag. It clamps into the hut's rotting beam like a claim, an act that ties data to memory."
        "Promise a nightly check-in to the co-op":
            "You make a small oral agreement — a nightly call, a shared logbook. Kaito's shoulders ease a hair; it's not policy, but it's a promise that counts for something."

    # --- merge ---
    "Small acts accumulate into the scaffolding of trust. You scribble a list in your notebook—deployment sites, sensor IDs, responsible persons. The handwriting is cramped with speed. Each item is a promise to watch, calibrate, and, if necessary, fight."
    "Small acts accumulate into the scaffolding of trust. You scribble a list in your notebook—deployment sites, sensor IDs, responsible persons. The handwriting is cramped with speed. Each item is a promise to watch, calibrate, and, if necessary, fight."
    # [Scene: TideLine Field Office | Night — After Signing]
    hide dr_lian_obasi
    hide kaito_navarro
    hide marin_sol

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Dissonant piano, building in tempo]
    # play sound "sfx_placeholder"  # [Sound: The distant patter of rain; the soft zoom of a tablet being read]
    "Later, when the field office quiets and the building's hum goes to low gear, Jun finds you by the last lamp. His movement is furtive; his face is younger in this light, the sheen of corporate"
    "calm cracked by something else. He leans close enough that his breath is a small wind."
    show jun_park at left:
        zoom 0.7

    jun_park "Marin—there's a paragraph I didn't want to read aloud in front of everyone."
    show marin_sol at right:
        zoom 0.7

    marin_sol "What is it?"

    jun_park "Indemnity. There's wording that shifts liability beyond immediate maintenance—it's broad. And there's a clause about shoreline rights—if a 'protective structure' is deemed necessary, there's a framework that could be used to assert company stewardship over certain access points."
    "His words are a blade under the lamp: small, precise, and capable of changing the contour of everything you've just signed. The room seems to contract around them. Your heart pounds like a signal drum, a"
    "high steady beat. The urgency spikes and the negative hedges in: this is the moment where good intentions meet legal architecture."

    marin_sol "Show me the clause."

    jun_park "I— I didn't see it as clearly before. The relief of funding dimmed the glare."
    "You scroll. The legalese is dense, syntax bred to bury meaning in parentheticals. Your eyes feel sanded by the words. 'Indemnify,' 'limitation of liability,' 'assignment of easements upon material failure'—phrases like incantations. Your breath shortens; the world tilts on that thin hinge between precaution and concession."

    marin_sol "This could be leveraged to privatize access if one interprets 'protective structures' as permanent. Or to require our co-op to sign maintenance terms that erode community control."

    jun_park "I— I didn't see it as clearly before. The relief of funding dimmed the glare."
    "You stare at the text until the characters blur into a low tide of implications. The high arousal of the chapter surges: a hot, anxious knifepoint where the promise of safety smells faintly of sale."
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "We can model outcomes. If we run scenarios on legal contingencies and overlay them with coastal usage maps, we can quantify risk."

    marin_sol "We need a legal review. An outside counsel. Public transparency. And—' (you close your notebook slowly, the sound small and decisive) '—we need to make this a living document, one we can amend in public."
    "Your voice, which has been steadfast and technical, tightens at the edges. The guilt that has driven you so far becomes a sharpened promise: to read, to watch, to fight clauses before they become dirt lines. You feel the pull of responsibility like a current, and it isn't calm."
    hide jun_park
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "If they privatize access, it's not just property they're taking. It's our right to dawn and sea."

    marin_sol "Then we stop it. We make the MOU conditional on a legally binding public-access guarantee. We don't let 'temporary' become 'permanent' by paperwork."
    "The room tightens with agreement and with the knowledge that words now have to carry weight against money and machinery. The arousal rides upward—fast, urgent—because the stakes have crystallized in a clause few read aloud."
    hide marin_sol
    show jun_park at right:
        zoom 0.7

    jun_park "I can help. I'll pull every clause again. I won't let this slip."
    hide dr_lian_obasi
    show marin_sol at center:
        zoom 0.7

    marin_sol "We will watch every clause. We will watch every deployment."
    "You make that promise aloud. The words are not victory; they are a pledge against erosion—of shoreline and of trust. Pride and fear cross in your chest. The negative tonal quality doesn't soften; it's realistic and"
    "anxious. The urgency has become kinetic: people will move, lawyers will write, sensors will go live. The first tests of that kinetic energy will arrive sooner than any of you want."
    hide kaito_navarro
    hide jun_park
    hide marin_sol

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings spike, then hold on a single, unresolved note]
    "You can see the timeline mapped in your head: procurement, deployment, sensor calibration, community meetings, legal reviews. Each milestone pulses with pressure. You feel the role you volunteered for—the one inked in grief and stubborn care—settle more heavily into your shoulders."
    "Page-Turn Moment: You look at the clause again, then at the signatures on the MOU. The lamp casts a thin glint where ink meets paper. Outside, the rain becomes harder, a sound that could be any"
    "near-future storm. You close the tablet, close the notebook, and the room seems to inhale with you. This is no resolution—only the first motion of a long wrestling: urgent decisions, legal tangles, and the constant vigilance"
    "you promised yourself when you came home."

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM crescendos, then cuts]

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
