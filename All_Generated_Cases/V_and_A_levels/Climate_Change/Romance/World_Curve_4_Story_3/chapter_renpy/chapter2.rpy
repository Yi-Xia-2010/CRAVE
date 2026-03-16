label chapter2:

    # [Scene: Tidewatch Lab | Midday]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, steady piano with soft ambient pads]
    # play sound "sfx_placeholder"  # [Sound: Hum of servers, distant gull cries, the lab's ventilation breathes]
    "You step in with the taste of salt still clinging to your tongue from the Promenade. The lab smells of ozone and damp paper; a strip of algae darkens the concrete at the threshold. Your ledger"
    "slides from beneath your arm onto the workbench, landing beside a printed stack of tidal curves. Your fingers—raw from tracing contours and redrawing shoreline overlays—leave faint smudges on the edge of the paper."
    "On the nearest screen, color bands ripple across a simulated coast. You run the marsh-restoration scenario again, watching the model fold in cordgrass, sediment trapping, and the strategic raising of a handful of homes. The curves"
    "nudge down, not dramatically, but enough: flood hours shorten, peak depths shave a margin that will make some houses survivable without a full buyout."
    "You let out a breath that isn't entirely relief—you know the numbers are only part of the story—but your chest loosens in a way that feels like permission. This is work you can touch. This is negotiation that begins with soil and ends with shelter."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft click of an incoming message; a phone vibrates on a metal tray]
    "You trace the compass's worn edge with a thumb until the metal is smooth beneath your skin. Marta's silicone band is imprinted in your mind—those coordinates she wears like a promise. You tap a key and"
    "pull up the community overlay: garden plots, raised walkways, the stamped lines where volunteers have already begun to move earth. The visualization fills the corner of the screen like a small, obstinate map of insistence."

    menu:
        "Annotate the margins with people's names and quotes":
            "You write brief lines beside the model—'Marta: windows on raised beds'—letting memory sit beside statistics. The ledger feels more human for it."
        "Tighten the technical notes and send the simulation to the grant portal":
            "You tidy the data, make the figures airtight. The file goes to the grant inbox with a quiet click; the model is cleaner, but the margins stay blank."

    # --- merge ---
    "Continue narrative after the interaction."
    "A soft knock, then the lab door opens and Noah Reyes slips in, carrying a rolled-up plan tucked under his arm. The curl of silver on the cord at his throat bobs as he gestures—his ring"
    "catching the light like an offering. He moves with the easy, practical optimism you always envy: approachable hands, a grin that says he believes things can be smoothed."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You're still here. Good—there's coffee in the thermos. And I brought the community layout you asked for."
    "You look up, and the lab feels warmer for the presence of another person. He sets the roll down and unclasps a paper with city markers, handwritten notes knitting together with printed parcels."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I ran the marsh-plus-raise sim again. It trims projected flood hours—small wins, but real ones."
    "Noah Reyes leans over the screen, eyes scanning the bands, then the ledger, then you. He runs a hand through his curls, thoughtful."

    noah_reyes "Small wins add up. Stories add weight to numbers, though. People remember that someone planted a garden, not a curve on a chart."

    asha_moreno "That's what I'm trying to balance—how to make the grant reviewers see both. How to make Mayor Rosa sign on without selling the waterfront away."

    noah_reyes "Lila will make it flashy. Metrics with LEDs. We need the heart next to the machine."
    "You find yourself explaining, slower than you usually speak, where marsh roots trap sediment, where raised foundations reduce entry points for storm surges, how volunteers can do the grunt work for a fraction of the cost"
    "of a full engineered wall. Your fingers drum the ledger as if coaxing the ideas into being."

    noah_reyes "Then we don't let them polish the edges off. We keep the stories rough; we put them in the grant application as testimony, as evidence."
    "The conversation twists like tide and shore—practical, slow, careful. He listens in the way he always does, letting you unload the technical anxieties and then picking out the human ones."

    menu:
        "Reach out and accept his coffee with both hands":
            "You take the thermos from him. His fingers brush yours for a second; warmth pulses through your palm and a small, private steadiness settles in your chest."
        "Thank him and continue annotating the plan":
            "You accept the cup but keep your pen moving. The contact is polite, functional; his presence is comfort, but you keep your rhythm."

    # --- merge ---
    "Continue narrative after the interaction."
    "You glance at a monitor showing a grainy clip Eli sent this morning: the Boatyard in motion. The camera favors his hands—callused, precise—as he bends ribs into shape; sawdust jets like confetti in the shaft of"
    "the afternoon. The smell of pine and resin folds into memory, and you imagine standing beside him, passing clamps, listening to the old jokes that make craft into ritual."

    asha_moreno "Eli's footage is good. It anchors things. People respond to work they can recognize."

    noah_reyes "Exactly. He shows up as evidence that we already have the muscle and the willingness. That keeps the lease-money sharks at bay."
    "You pause at his choice of words—your chest warms at the colloquial phrase, not because it is clever but because he is always finding the human metaphor to wrap the technical in. The lab's fluorescent light"
    "softens as clouds slide past the berm windows; outside, the Beacon's halo is a distant, cool star."
    "A notification buzzes on the lab's communal terminal. You watch as a name lights up on a shared calendar—Lila Park—followed by a short, crisp meeting invitation from a resilience consortium account. You feel a small sting, not of surprise but of stylistic friction: her presence is efficient, curated, inevitable."
    "Noah Reyes notices the micro-expression before you can hide it."

    noah_reyes "She'll be making the rounds. Hard sell, clean slides."

    asha_moreno "She'll make it easy to offer a quick, complete solution. That's the danger."

    noah_reyes "We can hold a middle ground—leverage their sensors, insist on local oversight clauses. Make it a partnership we can define."
    "You let his optimism land like ballast. It steadies without solving everything; it doesn't need to. There are municipal grants to meet, sensor feeds to integrate, volunteer teams to mobilize. The tangle feels less like a knot and more like workable rope now."
    "You stand, pushing back from the workbench. The papers rustle. Your fingers ache in a way that makes accomplishment tactile; the soreness is a reward."
    # [Scene: Raised Gardens | Midafternoon]
    hide noah_reyes
    hide asha_moreno

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low chatter, the soft clack of trowels, a distant kettle on a stall]
    # [Smell: Warm soil, citrus peels, an herbal tang]
    "You step into sunlight filtered through canvas awnings. Marta waves from between two planters—her hands stained with compost. You catch the clean scent of citrus from a nearby crate where someone peels mandarins for volunteers. Marta's"
    "silicone band gleams when she reaches for a spade; you don't need the exact numbers embossed on it to know what they mean. The band is a talisman: coordinates that point to where people sweat and"
    "remember."
    show marta_chen at left:
        zoom 0.7

    marta_chen "You're glowing. Is that the lab or Noah's coffee?"
    "You laugh, and the sound is easy, unshaped by the labor ahead."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "A little of both. The model shows hope. We can sell a grant with both soil and sensor."
    "Marta claps you on the shoulder in the way she always does—fast and fierce."

    marta_chen "Then let's make sure the grant hears the smell of citrus and the grit of the Boatyard. Bring the ledger to the meeting. Bring Eli's clip."
    "You tuck the ledger under your arm and feel the town fold into the gesture. The momentum is real: kids pestering for seed packets, volunteers swapping tips on salinity, a map pinned to a board with yarn running like little tide lines between initiatives."
    # [Scene: Tidewatch Lab | Late Afternoon]
    hide marta_chen
    hide asha_moreno

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Piano swells very softly, then steadies]
    # play sound "sfx_placeholder"  # [Sound: A phone on the bench plays a muted clip of Eli's hammering; somewhere, a municipal chime marks the hour]
    "Back in the lab, you and Noah go line by line through the grant narrative. He reads aloud while you make marginal notes—balance, brevity, heart. The exchange is practical and intimate: two voices shaping a public argument."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "We put volunteer labor in as matching funds. They can't ignore in-kind when it's visible. We list the sensor nodes as a condition, not a takeover."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "And we insist on a local review board—Mayor Rosa plus two residents and a technical advisor from the lab."

    noah_reyes "That sounds reasonable. It gives the town leverage."
    "Your throat tightens—not from fear but from the weight of responsibility you willingly took on. You have plans, partners, a ledger full of human margins. There is confidence here, steady and earned."
    "He reaches across the table and rests a hand on the rolled community plan. The gesture is small, deliberate."

    noah_reyes "Ask for help, Asha. You don't have to carry the whole town's history in one ledger."

    asha_moreno "I know. I'm trying to learn how."
    "Noah Reyes smiles, an expression that makes space for the failures and the attempts all at once."

    noah_reyes "Start small. Let someone else run the volunteer schedule. Let Eli handle hardware. You guide the vision."
    "You imagine the next steps in ordered frames: a volunteer meeting, a sensor deployment, Eli's hands clamping ribs, Mayor Rosa's signature in the margin. The day has unfolded like a tide—gentle, inevitable, advancing the shore in small increments."
    "Outside, through the lab's window, the Beacon's glass catches the grey and throws it back in a pale halo. You know the Beacon is where headlines will be made and bargains whispered. Lila's invites will be"
    "staged there; funders will like the clean lines and the interactive tide model. Your plan will have to be translated into that language."
    "You tighten your fingers around the compass on your ledger. You breathe in the lab's recycled air and taste salt that has traveled through the day, carrying voices and sawdust and citrus. The momentum in town is a quiet swell—hope measured in seedings and sensor nodes."
    "You fold a page, tuck the ledger under your arm. There is a next place to go, a different language to learn—the Beacon and its bargains. The thought isn't dread. It's a soft, steady curiosity: can"
    "you keep the town's voice intact in a room built to silence the rough edges?"
    hide noah_reyes
    hide asha_moreno

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Piano resolves into a gentle single chord, inviting the turn of the page]
    "You take one last look at the screens, at Eli's clip, at Marta's band, at Noah's patient steadying. There is a plan shaping itself in your hands—partial, imperfect, possible."
    "Page-turning thought: The Beacon will be formal and bright and strategic. It will be the stage where stories and sensors meet; where you'll have to speak both technical and human truth. You feel the quiet buoyancy"
    "of readiness—enough to walk into that light, not because the answer is certain, but because the town will need you there."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
