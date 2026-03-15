label chapter5:

    # [Scene: Drowned Orchard | Night — Storm]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, rolling cello undercut with distant percussion; a mournful wind motif threads through.]
    # play sound "sfx_placeholder"  # [Sound: A wristband chime, shrill and urgent. Rain stabs the wooden planks. The sea grinds like gravel.]
    "You know the tidal clock in your bones, but tonight the hours skip. The sky has folded into a black ceiling; the wind comes like a fist and takes its time squeezing. Salt and wet earth"
    "and the copper-smell of disturbed algae hit your face when you climb down onto the closest raised mound. Water slaps at the stilts, finding pockets of weakness you had hoped were just memory."
    "Your wristband tears itself from the quiet — three frantic beeps, then an urgent vibrato you have only ever heard during tests. Your thumb fumbles on the corner of its face and a thin readout blinks:"
    "anomalous frequency spikes along the barrier nodes. For a breath you do nothing but listen to the sound of your chest and the sea and the way both seem to be pulling away from you."
    "You taste guilt like metal. You remember the pilot that failed three seasons ago: the smell of wet wood, the voices at dawn, how you watched and swore you would not let it happen again. The memory is a tidal undertow you can feel tugging at your ankles."
    "Asha appears before you can decide to run — hair damp, lab glasses crooked, her technical vest smeared with mud. She moves like someone carrying a detonator and a prayer. In her hands she holds a tablet that flashes models and wavy lines."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "Mira — you need to see this. It's not a sensor glitch. There's a resonance band in the barrier's design. Under certain wave conditions it amplifies incoming energy instead of dissipating it."
    "You can hear how she is trying to stay clinical, how the words fight to keep panic out of their edges. But her knuckles go white on the tablet, and the line graph twitches as if it, too, is seasick."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Explain. Slow. What does resonance mean here? Show me the nodes."

    asha_mehta "The modular pylons — they're coupled to dampening plates. The coupling is fine at modeled frequencies. But with the off-season swell — higher energy, the angles of incidence shift — the system couples into a feedback loop. The barrier can reflect and magnify wave energy back into the bay. It's physical amplification. It's… dangerous."
    "Your throat closes. The word loops in your head. Dangerous. Your notebook — the pages so often a harbor — stays folded in your jacket. You keep thinking of Nadia's small hands around your sleeve, Ruben's"
    "cane rasping on the boardwalk, the mural Cassian and you finished two weeks ago, the bench where people leave shells for luck. Everything feels suddenly fragile."
    "From the shore, Cassian Rhys comes running through the sheets of rain — paint on his jacket like war stripes, sneakers spattered, hair plastered to his forehead. He skids to a stop, breath flaring, eyes flaring like embers."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "You told me the pilot bought us time. You told me transparency. What is this, Mira? How did this slip through review?"
    "You can hear accusation under his breath: it's personal. He means every syllable; his jaw is set. It's more than betrayal — it's the sudden exposure of hope that might have been false."

    mira_kestrel "Cassian— I didn't design the barrier. We negotiated oversight. Asha just—"

    cassian_rhys "Negotiated? We cheered and planted grasses while machines were being tuned to hum the wrong way? People slept easier because we said they could. Did you know?"
    "Your mouth opens. You want to explain the months of meetings, the clauses that snagged, the compromises you signed with a pen that trembled. The storm shreds your rehearsed words. Instead, you say the only true sentence that stands:"

    mira_kestrel "I didn't know. Not this."
    "Ruben stumbles up beside the overturned crate that once held seedlings, cane scraping; his breathing is a slow, hard rasp made of salt and night."
    hide asha_mehta
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "Mira. Child. You feel that? The water is talking. We don't argue with the water. We listen and we move."
    "His voice is an anchor and a rope. Nadia's small fingers are at your sleeve, wet and warm. She presses her forehead to your arm like a plea you can physically feel."
    hide mira_kestrel
    show nadia_kestrel at right:
        zoom 0.7

    nadia_kestrel "Don't let them take the schoolyard. Promise me."
    "The word 'promise' is soft as foam and heavy as a rock. Promises are the currency of this town; you have spent them and saved them and feared losing them. You taste salt and history and a knot of fear."

    "Engineer's voice" "We've got teams on the nodes. Jonah suggests a software tweak and a phased dampener install. We can patch the coupling in-site. We'll need a window to do it."
    "His tone is businesslike, which for a second steels you, then makes your skin crawl. You remember the consortium's contracts like fine print shadows: maintenance privatization clauses, phased funding tied to milestones, clauses that hand over long-term upkeep to contractors."
    hide cassian_rhys
    show asha_mehta at center:
        zoom 0.7

    asha_mehta "A tweak. That's not a fix; that's a stopgap. And who's funding the stopgap? The consortium. Who pays long-term? The town. Who owns the maintenance contracts? Private operators under governmental indemnity."
    "Jonah Hale arrives then, rain beaded on the broad shoulders of his water-resistant coat, hair neatly combed despite the storm, the kind of composed in a weather that makes you think of engineered certainty."
    hide ruben_ortega
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Mira. Asha. We've modeled contingencies. There are adjustments. If we accept a moderated footprint and phase in reinforced dampers, the barrier will perform within safety margins."

    jonah_hale "We can write protective language. Public-private maintenance can be structured with oversight. We have investors anxious to meet deliverables. We don't want to displace people. We want to avoid worst-case failure, Mira."
    hide nadia_kestrel
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "And the clauses? The maintenance privatization?"

    jonah_hale "I am trying to save as much as possible. Indecision kills people in storms. We make a call and execute it. Or we stall and watch the sea take more than it would."
    "The exchange becomes a tide of its own—arguments and counterarguments folding in and out, each trying to tug you toward a different shore."

    menu:
        "Cut through to the nearest node and read raw sensor logs":
            "You duck under a sagging walkway to the exposed node, fingers numb as you wrestle a cover loose. The raw telemetry stutters on your wristband — you copy a chunk into your notebook with shaking hands and feel slightly steadier, as if you have something concrete to hold."
        "Shout to everyone to move inland now":
            "Your voice thunders over the wind. Volunteers and neighbors look up, startled, then scramble. For a moment control returns — people obey. But someone calls back from the shoreline: 'We need your plan, Mira!' and your command feels thin."
        "Stay with Asha and parse the model together":
            "You stay. Between you and Asha the models become a little less abstract. You can trace the rising curve, see the nodes that will likely couple. It does not fix the hazard, but it gives you a shared map to point at when voices get loud."

    # --- merge ---
    "..."
    "The choices are small tasks against the larger tide. Each one steadies you in a different way: raw data, brute evacuation, or focused analysis. The storm does not care which you pick; it only cares that you move."
    "You choose — not yet the big decision, but a step that steadies the structure of your thinking. The rain slices through the small order you've created. Lights on the horizon flash: the Old Northpoint Lighthouse,"
    "engine lamps from Jonah's temporary crews, a lone volunteer's phone waving like a tiny beacon."
    # [Scene: Shoreline | Immediate — Wind-razed]
    hide asha_mehta
    hide jonah_hale
    hide mira_kestrel

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant cracking; a sound like a spine giving way. A low frequency thrum undercuts everything — the resonance rising.]
    "From the edge of the water you can see the pattern now: the barriers, meant to seam the sea, shimmer under the surge like a row of teeth. The thrum vibrates through your boots and into"
    "bone; your teeth feel loose with it. Asha pushes data into your hands — animation of interference patterns that look, in motion, unbearably like the thing it warns against."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "If a swell hits at phase X with a leftward angle off the promontory, nodes 7 through 12 lock in phase. That creates a standing wave — and the standing wave throws energy back into the orchard. It amplifies the bay's oscillations locally."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "How likely is phase X? How often do we see that angle?"

    asha_mehta "Not often. Off-season, but not vanishingly rare. Climate variability has increased frequency. We engineered on past expectations, but the new variability expands the envelope. Jonah's model used historic distributions; climate change rewrote the distributions."
    "Her words land like pebbles hitting a glass jar. The long arc of climate change — the thing you live inside every day — folds in here, a technical detail with life-or-death weight."
    show ruben_ortega at center:
        zoom 0.7

    ruben_ortega "It will not be the whole town at once. It will find the soft corners. The old margins. My boy's shack, the children's hut — those are where the sea will begin to take."
    "His cane taps a rhythm of history. He looks at you as if testing whether the weight of the town fits on your shoulders tonight."
    "Cassian Rhys moves closer, voice softer now, almost pleading."
    hide asha_mehta
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "If you pull the plug, Mira — town loses the funding. Jobs, the desal plant upgrades, heavy equipment for the berms. People who can't move will be left with nothing. But if you let them keep going and it fails…"
    "He can't finish. His wet eyelashes catch the lamplight like constricted crescents."
    "You feel the choices like currents around your calves. Each decision will wash someone away or save someone else. Your past — the failed pilot, your hesitation — presses against your ribs."
    "Jonah Hale's voice comes across the sand again, authoritative, practical."
    hide mira_kestrel
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "We can accept a moderated compromise: smaller hard footprint, phased dampeners, immediate temporary reinforcements. It will spare many homes. Yes, some neighborhoods at the soft margin will need to relocate. We can prioritize vulnerable households for relocation assistance. We minimize displacement."
    "His solution is a ledger of reduction; it slices the problem into acceptable losses. There's a cold logic to it that tastes of math, not of memory."

    "Asha, furious now, says what you have been thinking and not wanting to let loose" "Accepting this without an independent review hands long-term maintenance and cost burden to private operators. It sets a precedent. It doesn't fix the resonance. It buys a version of safety that may only be surface-level."

    jonah_hale "And refusing it risks the whole project collapsing, losing everything at once."

    cassian_rhys "Or exposing the flaw risks that they walk away and we have nothing but our hands. People will go hungry. We'll litigate for years."
    hide ruben_ortega
    show asha_mehta at center:
        zoom 0.7

    asha_mehta "There is a middle: emergency independent review, a temporary hold on construction, a transparent redesign. It slows us, but it buys safety with oversight — if the political will and funding cushion it."
    "The air snaps with choices, each one tugging in a different moral direction. Your pulse is a drumbeat in your ears. You close your eyes for half a second and see the faces: the volunteer planting"
    "berms last month; Nadia's school under a new tarp; Ruben's laugh when the first seedlings took hold."
    "Nadia squeezes your sleeve so hard you feel the print of her small knuckles. She looks up at you with that particular, terrible faith only a child can give."
    hide cassian_rhys
    show nadia_kestrel at left:
        zoom 0.7

    nadia_kestrel "Do the right thing."
    "The simplicity of the phrase is a blade in your ribs. 'Right' is complicated tonight."
    "Your mind races through consequences in calibrated lists like Asha's models do — safety margins, displacement numbers, jobs — but your heart stacks names: Mrs. Leung's widow house; the snack stall by the ferry; the mural Cassian painted on the school wall. The ledger and the list keep colliding."
    "You imagine clawing at the contract language itself, tearing clauses until they bleed. You imagine standing at a podium and exposing the flaw to the region, watching investors recoil. You imagine the crowd at a public"
    "hearing cheering at Jonah's pragmatic calm because it promises immediate safety. You imagine being on the other side, watching seawalls hum and then break."
    "The storm's pulse ratchets up. In the distance, the Old Northpoint Lighthouse throws its lantern: a single, steadier beat against the manic sky. You feel, with a clarity sharpened by panic, that the choice you make now will define not only the pilot but the character of Lowry Bay."
    "Everything collapses into a single impossible node: accept Jonah’s moderated hybrid compromise; expose the flaw publicly and halt construction; or push for a transparent recalibration with an independent review and emergency redesign."

    menu:
        "Accept Jonah’s moderated hybrid compromise — prioritize immediate safety and scale back demands.":
            jump chapter6
        "Expose the flaw publicly and halt construction — even if it destroys funding.":
            jump chapter15
        "Push for a transparent recalibration: demand an independent review and emergency redesign.":
            jump chapter6
    return
