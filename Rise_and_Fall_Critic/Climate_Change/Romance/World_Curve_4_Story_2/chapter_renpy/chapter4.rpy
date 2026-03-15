label chapter4:

    # [Scene: North Beach Ridge | Early Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rasp of wind over dune grass, footsteps on compacted sand, distant gulls crying]
    # play music "music_placeholder"  # [Music: Steady, hopeful percussion; a soft swell that suggests work accomplished]
    "You taste salt with every breath, a fine grit at the back of your throat like a reminder that the sea is never polite. Dawn teeths the horizon with pale gold; the sky is the kind"
    "of washed blue that makes you think anything might still be coaxed back from the edge."
    "Around you, people make a rhythm so precise it could have been a machine — heave, tie, tamp, step back, measure. Ronan barks an instruction and laughs when someone misjudges a bag's center of gravity. Maya"
    "hauls a coil of geotextile past your boot, cheeks flushed, paint-smeared hands moving as if the work keeps her steady."
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "You okay? You look like you'd rather be in that greenhouse counting seedlings."
    show alys_maren at right:
        zoom 0.7

    alys_maren "I thought I would. But—"
    "You let out a breath that tastes of the sea and the little stack of council papers in Harrow Hall. 'This is where people need me.'"
    "Ivo Calder grunts and nudges a battered trowel toward you. 'Then help me tamp this frame. Your hands have more patience than mine for the fiddly stuff.'"
    "You press your palms to cold, damp sand. The texture bites through the gloves. It's honest work — measurable, immediate. The sand gives under your weight and then holds. There is a satisfaction in watching something"
    "that might have washed away yesterday stand because you and others put your bodies into it today."
    hide ivo_calder
    hide alys_maren

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clack of tools, a murmur of coordinated voices; a child's shout as a dog chases a ribbon]
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "Alys! Leyna's got a reading. You want to see the sensors by the rock outcrop?"
    "Dr. Leyna is crouched near a line of small foam buoys tethered to stakes. Her tablet screen is a field of blue graphs and tidy numbers. The sensors are the kind of pragmatic poetry you trust at 3 a.m. — blunt, precise, and unbreakable unless something very bad happens."
    show dr_leyna_ortiz at right:
        zoom 0.7

    dr_leyna_ortiz "Erosion rate's trending down near the pilot breakwater. The wave attenuation models are matching what we'd hoped — about a fifteen percent reduction in peak energy today."
    show alys_maren at center:
        zoom 0.7

    alys_maren "Fifteen percent is fifteen percent more houses that don't get flooded."

    dr_leyna_ortiz "Exactly. And that translates to livelihoods saved. It's not the endgame, Alys, but it's something you can show people before the next council vote."
    hide ronan_pike
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "Show, don't lecture. We fixed a pump last week, fixed someone's roof yesterday, and now they see rallying makes a difference. That's why they're here."
    "You watch a woman across the line fold a borrowed tarp into a makeshift shelter for a collapsed dune and feel the small, steady bloom of pride — not your pride, not Ivo's, but the town's."
    "This is what trust looks like: hands in the dirt, scars on knuckles, no grand speeches necessary."

    menu:
        "Check the tide chart again":
            "You pull your compass from your jacket, flip open the dog-eared tide chart, and trace the incoming swell. It reassures you — for now — because knowledge feels like leverage."
        "Call Maya over for a quick break":
            "You call Maya. She drops her coil and comes over, wiping sand off her palms. You share a thermos of strong coffee — its heat is small reassurance against the cold wind."
        "Lend Ronan a hand on the seawall":
            "You shoulder in and take the next shovelful. Ronan claps you on the back with a grin; the work's rhythm pushes worry to the periphery, where it becomes manageable."

    # --- merge ---
    "Continue"
    # [Scene: Old Lighthouse Rooftop Greenhouse | Late Morning]
    hide dr_leyna_ortiz
    hide alys_maren
    hide ivo_calder

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Leaves whisper, water trickles from misting nozzles, the distant low of the sea below the cliff]
    # play music "music_placeholder"  # [Music: Gentle strings overlaying the previous percussion; a sigh of respite]
    "You climb the narrow iron stairs until the wind becomes a distant percussion. Inside the greenhouse, it's another weather — humid, perfumed with wet soil and leaf sap. Seedlings turn their pale faces toward the glass, impatient for sunlight and something steadier than storms."
    "Maya is at a workbench de-salting a tray of shoots, her laugh a bright thread when you enter. She moves with a kind of intimacy that belongs to people who grew up coaxing small things into life."
    show maya_maren at left:
        zoom 0.7

    maya_maren "You should have seen Ronan trying to stack sandbags without watching his toes. He swore like a fisherman."
    show alys_maren at right:
        zoom 0.7

    alys_maren "Did he keep all his toes?"

    maya_maren "Mostly. He said he'd trade one for a better night's sleep."
    "You settle beside a tray, running a finger along a thin stem. Your fingers smell of salt and coffee and the faint metallic tang of tools. The seedlings are a promise on a microscopic scale: fragile, but stubborn."
    "Ivo Calder arrives moments later, wiping a smear of sand from his cheek. He leans against a bench and watches you with an expression that no words can quite map — satisfaction, fatigue, something that reads like relief."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "Leyna flagged a model update for later. Says she wants you both to look at the cross-section before we raise the secondary berm."
    hide maya_maren
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "If we layer the berm with this composition, it holds better against surge while letting seagrass recolonize. It's hybrid — short-term defense, long-term habitat."

    alys_maren "That feels like a real compromise. People see the wall and the seedlings both."

    dr_leyna_ortiz "Exactly. It's literally doing two jobs. And the monitoring network will tell us when to transition material or augment the habitat plugs."

    ivo_calder "You always think ten moves ahead, Alys. I like that you can see the future and still put your hands in the present."

    alys_maren "Because the present messes up the future if we don't. I won't choose between them if I can help it."
    "There's a pulse in his gaze; it's almost a question about whether you'll let him hold part of the present with you. You don't answer it aloud. Instead, you touch a seed tray and let the warmth of the greenhouse radiate through your gloves."

    menu:
        "Sketch out a labeling scheme for habitat plugs":
            "You reach for your notebook and sketch a quick labeling grid. Your methodical handwriting calms you; it gives Leyna data she can trust and volunteers instructions they can follow."
        "Step outside for a minute and breathe the cliff wind":
            "You step out onto the narrow ledge. The wind grabs your jacket and pins it against your back. For a moment the world is only sea and breath; you feel steadier when you return."

    # --- merge ---
    "Continue"
    # [Scene: Harbor | Afternoon]
    hide alys_maren
    hide ivo_calder
    hide dr_leyna_ortiz

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clank of a pulley, the murmur of conversation, a distant cry of gulls]
    # play music "music_placeholder"  # [Music: A broad, warm chord; community hymn to effort]
    "You walk the line of the harbor as people secure the day's work. The seawall prototype — timber frames and rooted matting — holds back the first flirtation of the incoming tide. Children run along the"
    "quay and climb on stacked pallets, their shrieks like punctuation. There's cheering when a heavy roll of geotextile clicks into place and the tide abates against it."
    "Celine Harrow stands near the town's docking office, her posture composed, hands folded where the afternoon light falls on her lapel pin. You can't read her expression beyond being composed; it's the kind of look that could mean approval, calculation, resignation, or anything between. It is, by design, complex."
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "Alys. Ivo. The harbor looks…different today."
    show alys_maren at right:
        zoom 0.7

    alys_maren "Better. People feel safer."

    celine_harrow "Visible safety is important. Voters like what they can see. I've spoken to a few donors. They like movement."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "Movement that protects people now matters."

    celine_harrow "We all want the same thing. Different paths, same destination. Keep me apprised of test results."
    "You feel something like a bridge being built and dismantled at once. Celine's words are polite currency; her presence is ballast. She watches the seawall without saying more. Her gaze slips to you and then to"
    "Ivo; there is no tremor you can claim as promise or threat. Her reaction sits as 'Complex' — neither warmth nor outright opposition."
    hide celine_harrow
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "Sensors are already broadcasting. We should have preliminary flow data by tonight. If the attenuation is consistent, I can pull a brief for the council that shows real numbers."

    alys_maren "Then people can see — not just feel — that what we did mattered."

    ivo_calder "And we'll need to keep at it. Reefs, berms, shelters. It's a lot of sweat."

    alys_maren "It's a lot of people."
    "There is laughter, and it feels less fragile than it might have weeks ago. The harbor's edge hums with companionship threaded through labor. People trade tools, hand off sandwiches, borrow a plank and promise to return"
    "it. You think of the long list you keep in your notebook and how, today, the list looks less like an immovable ledger and more like a map that's being traced into reality."

    menu:
        "Offer to write up a short, public-facing report":
            "You volunteer to draft a simple field report with photos. People appreciate having the story of what they did — it turns effort into history and history into leverage."
        "Walk the seawall with Leyna to mark sensor points":
            "You and Leyna walk the line, marking sensor placements with bright ribbon. The markers flutter like small flags of progress against the wind."

    # --- merge ---
    "Continue"
    hide alys_maren
    hide ivo_calder
    hide dr_leyna_ortiz

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The harbor bell rings once; voices dip to a contented murmur]
    # play music "music_placeholder"  # [Music: Swells into a hopeful cadence; strings and low brass forming a promise]
    "You stand at the quay, the day's dust and salt settling into the weave of your jacket. The seawall holds — for now — and the town's breath seems to steady around it. People cluster in"
    "small knots, talking about shifts, about who will stand watch tonight, about scouts for the next material drop."
    "Ivo Calder leans close when the light narrows to a strand of molten orange. 'You did good work today,' he says, half a whisper, half a statement of fact."
    show alys_maren at left:
        zoom 0.7

    alys_maren "We did."
    "His hand briefly finds the small of your back — not possessive, but present. It is a contact that grounds a future you are trying to make possible. You feel an easing — not solution, but momentum."
    "Dr. Leyna calls you over to look at the latest feed. The graphs are a little steadier than they were in the morning. Numbers line up into a short sentence: the pilot defenses are working within their design envelope. There's a tidy, scientific sort of joy in that."
    "And yet — the ocean keeps its calendar. Leyna glances toward the horizon where a smear of cloud, low and fast, crawls across the sea surface."
    show dr_leyna_ortiz at right:
        zoom 0.7

    dr_leyna_ortiz "A swell front is due to come in tonight. Not a full storm, but a surge window. If the models hold, our berm should attenuate the surge enough to protect most of the houses along North Ridge."

    alys_maren "Mostly?"

    dr_leyna_ortiz "Mostly. That's why—"
    "She meets your eyes with that directness only data can afford."

    dr_leyna_ortiz "We need to decide whether to shift volunteers to reinforce the secondary line tonight or leave them to rest until daylight. Either way, it's a test."
    "The harbor seems suddenly smaller, the chatter distant. You can feel the geometry of the day folding toward a hinge. The seawall has bought you trust and time, but the sea keeps asking for proof on its own terms."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "We can hold it if we're there. But if everyone sleeps and the swell hits harder than the model says, we risk the worst of last season."
    "Celine Harrow watches from the lip of the quay; her face is unreadable, and so it remains — complex and private. You think of budgets and seedlings, of Leyna's graphs and Ronan's grin. You think of"
    "Maya's hands. You think, not least, of the houses that sit just behind the ridge, low and priceless."
    "Your notebook is in your pocket. Your compass rests against the metal of the rail. You feel the town's attention like a tide pulling at your bones — practical, expectant, hopeful."
    "A decision waits: to hold the line tonight with bodies and watchfulness, or to conserve strength and double down at first light. Both paths have weight; both are honest. Both demand something you cannot give equally."
    "You close your fingers around the brass compass and the metal is cool and steady, an anchor."
    "You rise, because leadership is less the crack of thunder and more the steady motion after. You are tired; everyone is tired. But the tide until tomorrow gives you time to choose."
    hide alys_maren
    hide dr_leyna_ortiz
    hide ivo_calder

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: A single sustained hopeful chord that opens like a door]
    "You think, for a heartbeat, of everything that happened today — the laughter, the mud, Leyna's numbers, Celine's quiet watch, Ivo's steady hands — and know that whether you tell them to hold or rest, the town has already changed. The work has become trust; the trust has become momentum."
    "There is a hinge ahead. You can feel its shape ahead of you, as certain as the pull of the tide."
    "You look at the line of volunteers gathering their jackets and flashlights. You watch the seawall's shadow embrace the incoming water. You breathe, and the breath is full of salt and possibility."
    "You are about to call the meeting to decide."

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: The chord swells and then softens, sustaining anticipation — not dread]
    "You step forward, voice steady, the town folding toward you like a practiced bell."
    "You are asking them to choose how to meet the night."

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade out]

    scene bg ch4_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
