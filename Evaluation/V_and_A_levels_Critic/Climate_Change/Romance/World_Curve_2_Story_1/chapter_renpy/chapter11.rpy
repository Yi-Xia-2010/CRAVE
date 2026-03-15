label chapter11:

    # [Scene: Municipal Hall — Council Chamber | Late Afternoon]

    scene bg ch11_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense strings under a staccato percussion; a heartbeat-like bass]
    # play sound "sfx_placeholder"  # [Sound: Rain tapping hard; the low roll of distant thunder]
    "You come in with the weight of the plaza still on your shoulders—the mutter of banners, the wet smell of cardboard pamphlets, Mateo Alvarez's breath warm with rain against your cheek. Here, under the council's high"
    "windows, everything feels magnified: the clauses, the promises, the people who will be split by whatever ink dries on these pages."
    "Councilor Rosa sits at the head, fingers steepled, her shawl damp at the edges. Etta is a small, stubborn presence pressed into a folding chair like a seed that refuses to let go. Elio Sato is"
    "near the projection screen—calm, efficient, the room's fluorescence catching the edge of his trench coat like a halo of cold light. Jun leans back, arms crossed, eyes focused on the door as if storms might sweep"
    "in and take him away. Mateo Alvarez stands by the window, hands deep in his pockets, jaw set."
    "Your tote with the camera and notes is heavy in the crook of your shoulder. You set it down and let your palms flatten on the council table. The paper feels slick under your skin."
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We have a full day. Elio Sato, you have the firm's draft. Etta, you have proposed covenants. Ari Tanaka—' (a small nod) '—we'll rely on you to translate neighborhood concerns into the committee language."
    "You feel that familiar, sharp intake of breath: they are asking you to carry more than documents. You're being asked to shepherd voices into sentences sturdy enough to survive lawyers. The word 'responsibility' thrums through your ribs like a bell."

    "Etta leans forward. Etta" "People did not build this town to be walled off. We need covenants that keep our lands public—no privatized seawalls that cut access. We need cultural protections. We need guarantees that the nursery lands and the fishing paths stay for everyone."
    "She looks at you, and in her hazel eyes is the memory of a thousand seedlings pushed into sand. You remember the greenhouse's humid air and the insistence of small plants growing through salt. You remember promises made to people who cannot afford to be moved."

    "Elio Sato taps the tablet and a slide washes over the screen—graphs, timelines, construction blueprints. Elio Sato" "Speed and scale matter. The firm can deploy modular barriers within weeks. That mitigates immediate risk. Relocation offers are part of the package for those who choose it. Resilience bonds provide upfront capital to stabilize incomes while construction proceeds."
    "His tone is precise, like someone reading from a weather forecast: inevitable and unblinking. His eyes flick to you with the same steadiness—expectation baked into form."
    "You open your mouth to respond, then close it. There is a list of ways to say 'not enough' without sounding like a refusal to save people. The halo of courtrooms and contracts loops in your"
    "head. You think of Jun's boat, of the patch of marsh Etta showed you where juvenile crabs had started returning. You think of Mateo Alvarez's prototypes in the lab, blinking blue LEDs like tiny sentinels."

    "Mateo Alvarez clears his throat and steps toward the table, each movement measured as if he is deciding how much of himself to leave on the floor. Mateo Alvarez" "Speed isn't worthless. But walls aren't a cure. If we rely on structural fixes alone, we ignore the marsh's role, the livelihoods that depend on it. We're trading one failure mode for another."

    "His words land harder than you expect—public and raw. The room turns at once to him. For a beat, his face is unreadable—then something like regret tightens his mouth. He looks at you in a way that is both apology and distance. Mateo Alvarez" "Ari Tanaka, I—I've been pitching hybrid solutions, but I can't be the one to tell people to trust structures when their homes are at stake. I won't be a billboard for half-measures."
    "You feel a pinch—an intimate ache—sharp and small. The air between you seems to contract for a second, and you understand: Mateo Alvarez is stepping away to keep his hands clean for the work he thinks"
    "will actually protect people. Or he's protecting himself from being blamed when something fails. Either way, his withdrawal is another kind of storm."

    "Jun leans in. Jun" "We don't want handouts. We want to be able to fish, to plant, to not be fenced out. Resilience bonds sound like debt to me. Who owns those bonds? Who gets to say when 'resilient' is good enough?"

    "Etta's jaw tightens. Etta" "And what's 'choice' when the alternative is a flooded house? People's 'choice' becomes a market decision unless covenants are binding."

    "Elio Sato's fingers drum once. Elio Sato" "Binding covenants will add months to permitting. The firm cannot guarantee investors indefinite delays. Our timelines are what enable funding at scale. If the town imposes restraints that jeopardize deployment, legal remedies will follow."
    "The word 'legal' tastes like copper when it hits the air. An invisible ledger seems to open between you: commitments weighed against timelines, human lives balanced on clauses written by people who rarely get their hands damp with salt."

    menu:
        "Read Etta's covenants aloud, emphasizing community language":
            "You unfold Etta's pages and let her words fill the chamber. The terms sound intimate—laneways preserved, nursery lands in trust, public fishing rights codified. Heads nod slowly; a murmur of approval rises from the community members present."
        "Ask Mateo to outline the hybrid technical safeguards":
            "You gesture to Mateo Alvarez. He stands, pulls his notebook from his satchel, and sketches the buoy array on the table. The technical detail grounds the conversation but leaves a hollow where commitments to land use should be. Some listen, others frown."

    menu:
        "Hand Mateo the field notes and ask him to speak plainly about limits":
            "Mateo Alvarez takes the notes, breathes in salt, and says in a voice rougher than before, 'I can design safeguards, but only if the community keeps oversight.' His candor draws a tired applause and a skeptical frown from Elio Sato."
        "Walk the line with Etta and ask what 'safety' looks like to her":
            "Etta shows you a narrow path—an actual boat lane—that must remain open. She speaks of elders who fish at dawn and children who learn to wade. Her description turns abstract policy into faces. A hush falls over the group."

    menu:
        "Negotiate strict covenants protecting community lands and public access.":
            jump chapter13
        "Accept the company's baseline contract to ensure swift construction.":
            jump chapter17
        "Launch a public campaign demanding audits and transparency, delaying the contract.":
            jump chapter20
    return
