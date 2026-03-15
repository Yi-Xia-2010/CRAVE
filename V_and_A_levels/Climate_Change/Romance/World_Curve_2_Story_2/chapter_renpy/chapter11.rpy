label chapter11:

    # [Scene: Tidewatch Lighthouse & Rooftop Garden | Late Afternoon — Rain Approaching]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent percussion; a taut string line enters and refuses to let go]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls cut through the hiss of fine rain; metal clinks and a welder’s sing-song]
    "You still feel the warmth of the pendant at your throat from the rooftop bench where you sat last night—an ember against cold skin. The rain that began as a tentative finger has nailed itself into"
    "the world. It snaps at tarps, wets the hems of coats, beads on your field notebook until ink blurs like a threatened promise."
    "Elias 'Eli' Rowan calls from the far edge of the roof, his voice corrugated with wet and weld smoke. He stands between two apprentices, sleeves rolled, goggles up like a crown. Sparks paint halos around his hands."
    "You move through the greenhouse air—humid, green, the scent of wet thyme and salt—and the practical part of you measures tasks in degrees and minutes: align the gutter, check the microfilter mesh, weld the bracket to"
    "the parapet. The human part folds itself into the workbench and hands a wrench with trembling fingers. Both parts are needed. Both are frayed."
    "Grandma Hira kneels by a planter, soaking her shawl, pinching basil stems between careful, knobby fingers. Her hands smell of soil and rain; her laugh is small and brittle when she speaks."
    show grandma_hira at left:
        zoom 0.7

    grandma_hira "Good hands, good people. The plants don't care for contracts."
    "You smile because you have no words that won't sound like speeches. She tucks a sprig of rosemary into your pocket with the economy of ritual. The herb smells like memory and stubbornness."
    hide grandma_hira

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hollow thud of sandbags; someone curses under the wind; a child's shout is muffled by the rain]
    "Elias 'Eli' Rowan comes up behind you, breathing wet and warmed metal. He wipes a hand on his jumpsuit, leaving a salt streak on fabric. When he speaks, there’s a pulse in his voice—a careful tightness that says he’s holding back a dozen things at once."

    "Elias 'Eli' Rowan" "We can finish the last bracket before dark if we press the schedule. Naomi's sensors should be online by midnight if her team can get the uplink."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Don't push the apprentices into a rush. Let them learn the weld, not just the shortcut."
    "Elias 'Eli' Rowan frowns—not angry, just uneasy—then exhales. He moves to demonstrate a seam, voice softening into instruction. The students watch him like they watch tide charts: hungry, nervous, reverent."

    "Elias 'Eli' Rowan" "Okay, watch my wrist—steady, steady. Heat, not hurry."
    "You let him teach. Partly because you trust him, partly because you need the small human discipline of learning and being shown. His hands are sure. The apprentices copy and the metal takes its new shape. For a heartbeat there is only craft, only the world yielding to patient pressure."

    menu:
        "Ask Elias 'Eli' Rowan to slow down the schedule and run a full safety check":
            "You step closer and speak the words you’ve been carrying: slow down. He glances up, face a map of compromise, and nods—reluctant but agreeing to an extra inspection cycle."
        "Tell Elias 'Eli' Rowan to push the team—get the brackets in before the tide rises":
            "You press your thumb to the wet metal and give the go-ahead. Elias 'Eli' Rowan's jaw tightens; he bites a grin and speeds the apprentice's pace. The welder's sparks seem to match your quickened heartbeat."

    # --- merge ---
    "The workshop continues and the narrative proceeds from here."
    "The choice dissolves into motion and you feel its weight in the tightening of shoulders across the workshop. Whatever you decide at small scales now will ripple later."
    # [Scene: The Arbor — Workshop Floor | Dusk]
    hide mara_kestrel

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The steady drip from a misaligned gutter; the soft murmur of voices as neighbors compare notes]
    "Inside the Arbor, Dr. Naomi Park stands over a field tablet, data like cold light. She taps at graphs with an impatience that looks, for once, human."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "The pilot will work as modeled only if maintenance remains local and continuous. If management shifts to external control, performance degrades. We've modeled that."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I know. That's why the covenant insists on community governance."

    dr_naomi_park "The language you received—'performance-based release of funds'—is a tether, Mara. The developers can delay, withhold, or condition funds based on nebulous 'timelines.' It gives them leverage to demand changes to the pilot under the guise of meeting benchmarks."
    "Something inside you hardens at the explanation and then splinters: the scientist catalogs the risk; the neighbor imagines doors closing; the person who sleeps with a pendant against her throat pictures a community losing agency in small clauses."
    "Tess O'Malley arrives, breathless, her raincoat plastered to her fluorescent lanyard. She holds a stack of council notes like a shield."

    "Tess O'Malley" "I've read Livia's redlines. There's wiggle room. I can push for clarification at tomorrow's caucus, but—' She slides her eyes to Naomi, then to you. '—the political cost will be loud. Livia's allies will accuse you of obstruction. They can twist 'delay' into 'endangering jobs' on morning broadcasts."

    mara_kestrel "If the clause stands, the pilot dies slowly. If we tighten it, funding might freeze."
    "Tess O'Malley exhales like someone who has rehearsed both options until both are thin with use."

    "Tess O'Malley" "I can lobby. I can leak minor revisions to sympathetic journalists. But I can't promise the council won't fold under pressure. People need payroll now."
    "Your throat tightens. You imagine a mother at the fish smokehouse who can't hold on if payroll vanishes. You imagine Rafi's hands, stung by cold and salt, working for no assurance. You imagine the rooftop gardens wilting because someone somewhere decided a column didn't match a schedule."

    menu:
        "Ask Tess to quietly draft strengthened clauses and hold them until the pilot is more demonstrable":
            "Tess nods, relieved to have a plan. She ducks into a corner and starts drafting language—careful, legal, patient. You feel a small thing arranged in the world, like a seed tucked into soil."
        "Tell Tess to take the fight public now—leak the loopholes to force a town conversation":
            "Tess's face shifts. She bites her lip and looks at you like someone evaluating a cliff. 'If we go loud, there will be fireworks,' she says. She leaves to make the calls before the rain drives her back."

    # --- merge ---
    "The choice courses through the room like electricity and the narrative continues."
    "The choice courses through the room like electricity. You can feel the pilot’s fragile architecture in the balance between hope and law."
    # [Scene: Edge of the Alley — Modular Breakwater Installation | Night]
    hide dr_naomi_park
    hide mara_kestrel

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide yawns against the pilings; the town's heartbeat is the thud of hammers and the mutter of cold breath]
    "You stand where the alley meets the sea. The new modules flex against the push of water, their seams imperfect but promising. Neighbors—arm-in-arm, soaked through—cheer on small victories like survivors marking distance walked. The breakwater is not glory; it is stubbornness."
    "Livia Chen appears under an umbrella, immaculate despite the rain. Her trench coat sheds the wet in precise, practiced curves. She holds the covenant papers like a talisman. When she smiles, it is the kind of smile that can be both warmth and calculation."
    show livia_chen at left:
        zoom 0.7

    livia_chen "You're doing fine work, Mara. The pilot looks promising."
    "Livia's eyes are steady. They are used to measuring things that scale. They are used to deciding who gets to stay and who must leave in the math of progress. Tonight, she is both compliment and danger."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "The clause about 'performance'—it gives developers veto power if 'timelines' slip. That's not a safeguard. It's a sledge."
    "Livia Chen's smile thins. She draws the umbrella tighter as if shielding a flame."

    livia_chen "We had two paths to funding. This term convinced investors we could hold timelines and accountability. Remove it and you risk the entire tranche. I won't pretend there aren't trade-offs. But we need money to scale anything that works."

    mara_kestrel "You're asking us to sign away oversight for the promise of money."

    livia_chen "I'm asking you to accept a pragmatic step. The pilot exists because we compromise. The town cannot survive on theory."
    show dr_naomi_park at center:
        zoom 0.7

    dr_naomi_park "Pragmatism without guardrails becomes co-optation."

    livia_chen "The alternative is no pilot. No jobs. No infrastructure. We all saw what happens when nothing is done."
    "Elias 'Eli' Rowan stands beside you, his face shadowed and unreadable. You cannot tell—by anything he says or how he holds his shoulders—whether he is calculating the engineering risk, measuring political cost, or silently counting the"
    "ways compromise might fracture the two of you. His look is, as it often is, complex."

    "Elias 'Eli' Rowan" "I don't like the clause, Mara. But I also don't want the welds to stop. People are counting on this paycheck."

    mara_kestrel "So do I. So do they. But at what price?"

    "Elias 'Eli' Rowan" "We defend it as we go. We tighten where we can. We show the model working and force the clauses to become redundant."
    "His plan has the smell of hope. It also smells of deferral."

    "You think of Rafi's question—echoing in the rain" "Can anyone hold power accountable?"
    "Tess O'Malley pushes through the crowd, eyes raw from cold and last-minute council meetings."

    "Tess O'Malley" "Council will vote tomorrow at ten. I can push for clarifying language but—"
    "Livia Chen folds the papers into a neat rectangle, as if a crease makes a promise truer."

    livia_chen "Sign now. We begin the pilot. Prove it. Then we renegotiate from a position of results."

    dr_naomi_park "Or you sign now and their 'results' are used to justify changes that hollow the pilot."
    "The conversation stalks the edges of civility and tears into a private fight in public. The rain increases. The sea answers with a higher, harder voice. The town's lamplight trembles like an ember uncertain whether to go out."
    "Your role as broker, as engineer of a bridge between ideals and funding, frays like rope under salt. You have never wanted power. You wanted responsibility. Now they blur."
    "Your heart pounds so loudly it becomes another instrument in the storm's orchestra. You can taste iron and salt. The world narrows to the papers in Livia's hands, the wet string of your pendant, the apprentices' fingers, Rafi's posture across the alley, Elise's unreadable face."
    "You are aware: this is a hinge moment. Small legal phrasing will act like a fulcrum. A single clause, slippery with legalese, could pivot the town into protection—or into sale."
    "Dr. Naomi Park takes a breath; the scientist's voice, usually precise, is ragged with something like fear."

    dr_naomi_park "If you sign without tightening that clause, it will be exploited. If you fight, the money may vanish. If you go public, you risk the narrative turning on you. We are in the room where fate is negotiated by commas."
    "You taste the word 'betrayal' like copper."
    "Elias 'Eli' Rowan reaches for your shoulder—light, a question. His fingers rest there for a beat that is too long and not long enough. The intimacy of touch becomes an unsteady counsel."

    "Elias 'Eli' Rowan" "You do what you have to, Mara. But don't let them make you carry the blame alone."

    mara_kestrel "I won't let them make us the scapegoats for trying."
    "Elias 'Eli' Rowan's mouth tightens and he looks away, toward the sea as if it will answer him. His reaction is complex; you cannot tell whether he braces for communal collapse or for the splintering of a private thing."
    "The storm climbs. The town's edges blur with rain and decision. Somewhere a radio crackles; a talk host promises thunder both meteorological and political."
    "An inner furnace you had kept low—practical resolve seasoned with stubborn hope—now flares into a harsher heat. The VeryNegative edges of the evening press against you: betrayal feels likely, collapse feels close, the notion of losing"
    "pieces of the town like planks pulled from a boardwalk takes residence under your ribs. Your breathing accelerates. The arousal is a drum—fast, relentless."
    "You look at the covenant in Livia's hand. The clauses are neat and fatal in the way paper can be. You think of Grandma Hira's rosemary in your pocket and the apprentices' hopeful faces and Tess's weary courage."
    "The choice is brutal and immediate. Each path risks harm: quiet erosion, drawn-out legal warfare, or public scandal that could split the town like lightning through old wood."
    "You have to decide."
    # play music "music_placeholder"  # [Music: The percussion collapses into a single, high metallic scrape—an auditory cliff]
    # [Scene: Tidewatch Lighthouse Rooftop | Night — The storm is now a living thing]
    hide livia_chen
    hide mara_kestrel
    hide dr_naomi_park

    scene bg ch11_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain like a hundred fists; a distant siren; the sea breaking sharp against the new modules]
    "You place your hand on the wet paper. The inked sentences look like teeth. They bite."

    menu:
        "Sign the covenant to keep the pilot running.":
            jump chapter12
        "Demand and fight for stricter legal clauses.":
            jump chapter16
        "Expose the loopholes publicly to force transparency.":
            jump chapter18
    return
