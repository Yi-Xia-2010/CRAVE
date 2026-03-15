label chapter7:

    # [Scene: Rooftop Gardens | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of conversation, the occasional clink of tin cups, distant gulls over the water.]
    # play music "music_placeholder"  # [Music: Warm guitar motif with light hand-drums, rising gently]
    "You can feel the day collecting itself into a single, practical joy: tools, soil, voices folding into one another. The rooftop smells like turned earth and lemon peel from someone's thermos; salt rides the air as"
    "if reminding everything where it came from. Your waterproof notebook is in your back pocket, the blue thread at the seam a steady presence under your palm."
    "Asha stands on a low crate with a bright megaphone, checking its battery like a conductor tapping a baton. People orbit her—students with paint on their sleeves, fishers with callused fingers, elderly neighbors wrapped in scarves"
    "against a drizzle. Theo crouches beside a makeshift display of tablets and a looping graph; his screen flashes 'StormRunoff vs. GreenGrid — Comparative Mitigation.'"
    show asha_patel at left:
        zoom 0.7

    asha_patel "Alright, team. Micro-demos up front—cisterns, bioswales, living shorelines. We show them how water moves when it's invited to stay. We dangle the metrics and the memories at the same time. Maya—you're with the speakers, yes?"
    "You breathe and answer with the thing you haven't stopped rehearsing in your head: the stitch you want to make between models and memory."
    show maya_calder at right:
        zoom 0.7

    maya_calder "I'll open. Short, local, and practical. We let the data back us up, but the stories bring it home."
    "Asha smiles—sharp, bright, absolutely in her element."

    asha_patel "Perfect. Elias 'Eli' Maren, harmonica cue; Theo, keep the feed live. Rosa, you sit with the elders. Make sure the fishermen get their piece—literal and metaphorical."

    "Elias 'Eli' Maren" "I'll play something that makes the gutters feel like music. Promise I won't make you cry before lunch."
    "You almost tell him you would accept the tears—they are the honest kind—but you settle for the small, steadying smile that tells him you'll hold the room."
    hide asha_patel
    hide maya_calder

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The megaphone hums; the harmonica breathes a bright line through the air.]
    "You walk the line of demonstrations, touch each element like a person being greeted. A cistern—painted by students—catches the first run-off from a chained tarp. A bioswale channels a trickle through native grasses, the water slowing"
    "and sinking where it can. On a low scaffolding, a mock 'living shoreline' of coir logs planted with salt-tolerant grasses rustles like a miniature dune."
    "Theo leans in, thrusting a tablet toward you. His graph pulses as real-time sensors—one in the cistern, two in a fake gutter—send numbers up."
    show theo_baines at left:
        zoom 0.7

    theo_baines "Look. Ten minutes post-simulated shower and the distributed systems are already diverting forty percent of the runoff compared to the baseline model. If we scale this—"
    "He is excited in the way only someone who sleeps with a coffee-stained hoodie can be—numbers alight in his voice."
    show maya_calder at right:
        zoom 0.7

    maya_calder "Point out the confidence interval. Emphasize that it's both measurable and deployable by residents. Not just 'nice to have.'"

    theo_baines "You're running my notes now."
    "He ruffles his hair and taps the screen to project small charts on a makeshift cardboard easel. Students gather, leaning to read axes and legends, and you watch technical language dissolve into the slow smile of someone who has just learned a useful trick."

    menu:
        "Tie Elias 'Eli' Maren's scrap of cloth to the railing":
            "You pull the cloth from Elias 'Eli' Maren's hand and loop it around a rusted nail. The movement is tiny but it settles something in your chest—an old promise given a new shape. People notice; someone mutters that they'll bring their own ribbons next time, and the cloth becomes a token in the breeze."
        "Use the scrap to tie a toolbag to the cistern scaffold":
            "You knot the scrap around a bag of seed packets and gardening gloves, securing the tools where they're needed. The practical choice draws a few approving chuckles—it's a small, visible claim that these things are built for use, not for ceremony. Elias 'Eli' Maren pretends to be affronted and then lobbed a mud-dappled smile at you."

    # --- merge ---
    "The demonstration continues with the crowd engaged and the work proceeding."
    "Asha's voice rises into the megaphone, warm but precise."
    show asha_patel at center:
        zoom 0.7

    asha_patel "Neighbors—this is not theater. This is learning. Come try the bioswale with us. Put your hands where the water goes. Tell the story you remember of the tide—how we used to welcome it, or how we tried to keep it away. Then tell us what you'd want to keep, and what you'd be willing to change."
    "Hands go up: a wrinkled fisherman offers a weathered cap; a student asks about maintenance; a mother asks if children can plant. You pass around gloves, sharing the slightly metallic smell of the compost mixed with sea-salt, and each pair of hands becomes a small ceremony."
    hide theo_baines
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "When I was your age, we learned the water by smell. If it takes sweetness, it's coming from the west. If it tastes like iron, there's something burnt upstream. You learn a place. You don't let someone else tell you what it is."
    "An elder fisherman, gnarled hands folded like something made to mend, starts into a story about a time the harbor remembered its old shape. People lean in, and the technical graphs on Theo's board find a new context—rooted in memory, not just modelled scenarios."
    "Elias 'Eli' Maren wanders the perimeter, harmonica tucked into his shirt, and he intercepts someone who doubts the scale. He listens more than he speaks, and then, when words won't land, he plays a simple line—the kind that makes a sentence feel framed, not finished."

    "Elias 'Eli' Maren" "Look, I'm not saying a garden replaces a wall in every place. But I've seen a roof feed a family when the truck routes were cut. We can be practical without being small."

    "Skeptic" "And if the storm is bigger than a garden?"

    "Elias 'Eli' Maren" "Then we make the gardens part of the answer. We make them stubborn. We teach them to hold more than soil."
    "The exchange is small, but the crowd loosens; the sceptic rubs his chin and helps a kid plant a plug of grass."
    hide maya_calder
    hide asha_patel
    hide rosa_calder

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft paper rustle as a press kit is consulted.]
    # play music "music_placeholder"  # [Music: The guitar motif swells, strings lifted into a hopeful chord]
    "You spot Dr. Sienna Kade among them, set apart by posture as much as clothing. She studies the setup like a machine inspecting a smaller machine—eyes narrowed, mouth unreadable. Her expression is complex: something between evaluation"
    "and an oddly furtive interest you cannot label. It is not the dismissal you feared; it is not quite acceptance either. You hold your breath long enough to feel the pause in your chest."
    show dr_sienna_kade at left:
        zoom 0.7

    dr_sienna_kade "Collect their data outputs. Cross-reference the models. We need to know where to fold and where to fortify."

    "Colleague" "Should we intervene? Invite them into the lab?"

    dr_sienna_kade "Not yet."
    "There is an unspoken calculus in her tone; you cannot tell whether she's buying time, recalculating strategy, or simply cataloguing. The ambiguity keeps her from being a defeated antagonist and keeps the scene supple—an opportunity, not a verdict."
    "Theo sidles up to you, eyebrows raised."
    show theo_baines at right:
        zoom 0.7

    theo_baines "She looks... complicated today. Which is better than villainous, right?"
    "You let out a humorless little laugh."
    show maya_calder at center:
        zoom 0.7

    maya_calder "I'll take complicated over villain any day. It means we can still speak to her logic."

    theo_baines "Then speak it loud. I'm streaming our metrics to the community server and tagging the resilience authority. If they want the numbers, they're getting them raw and public."

    maya_calder "Good. Make sure the axis labels are readable. Don't hide confidence segments in jargon."
    "Theo salutes you with a stylus like a weapon and hustles away. The run of the demonstration continues, a thousand small pivot points knitting into a larger shape. You wander, listening—each conversation a filament in the braid you're making between science and story."

    menu:
        "Step up to the crate and give a short, personal speech":
            "You climb the crate. The wood creaks familiar under your boots. You speak about your mother, about nets and tides, and about why small gardens matter to people who have always read the sea. The crowd leans forward; someone begins to clap with wet palms. Asha signals the harmonica, and your words feel humbler and stronger when carried by music."
        "Stay down in the crowd, answering questions one-on-one":
            "You stay among the people. You kneel to explain basin routing to a couple of teenagers and let the conversation swell slow and wide. They ask blunt, practical questions and listen when you answer. The intimacy feels like building the plan from the inside out—slower, messier, but rooted."

    # --- merge ---
    "The afternoon continues with both public address and intimate instruction blending into the outreach."
    "You do both over the afternoon—brief declaration from the crate, long, warm conversations at ground level. You learn that organizing is less about a single compelling moment and more about leaving an invitation in people's pockets: a chart, a handhold, a planted seed."
    "By dusk, the promenade has taken on the look of a place that has been re-told into being. Mud-streaked sneakers stand beside polished shoes; a child waves a ribbon in the wind near the railing where"
    "someone tied a scrap of cloth. Theo's graphs glow faintly under the string lights; the live stream has comments in three languages and a steady trickle of small donations for seed stock."
    "Rosa leans toward you, the smell of smoked fish on her, and squeezes your wrist—harder than diplomatic counsel, softer than command."
    hide dr_sienna_kade
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "You did right, Maya Calder. They listened. That's how you keep a place. You don't let it be built around you without telling it your name."
    "It feels like a benediction. You let the warmth settle into your chest; your shoulders drop, not in defeat but in acceptance of the weight you carry together now."
    "Elias 'Eli' Maren sidles up, harmonica resting on his lip."

    "Elias 'Eli' Maren" "So—next? We make noise. Strategic noise. Music, data, lunch for volunteers, a petition tied to every cistern. Theo can make numbers sing. Rosa can tell salt stories to anyone who will stand still, and Asha... Asha will make everyone feel brave."
    hide theo_baines
    show asha_patel at right:
        zoom 0.7

    asha_patel "And Maya? Will you lead the next 'how-to' on living shorelines? We get more hands, more roofs. We keep the stories and the soil."
    "You look over the crowd—students cataloguing plant species, elders crackling with approval, officials watching through the blur of community life—and your chest swells in a way that is almost painful with possibility."
    "Your internal monologue traces the shape of what's next: expand the demos into a temporary policy—a living proposal that the city cannot ignore because it is already feeding people, because it has already become a place"
    "people know by smell and name. You imagine Theo's graphs in a council chamber, but before that, you imagine the same graphs printed and stapled to volunteer packets, handed out with a cup of coffee and"
    "instructions that do not require jargon."

    maya_calder "We'll do it with music and coffee first. The lab comes later, if it must. This—' you sweep your hand across the makeshift neighborhood of gardens and people, '—this is what keeps us honest."

    "Elias 'Eli' Maren" "Music and coffee are my two specialties. Consider me on staff."
    "You feel the rising current of the crowd like a tide that demands to be noticed but also guided. The energy is electric and quiet at once, braided through soil and speech. It is the sort of swell that promises change by accretion: small, steady, human."
    hide maya_calder
    hide rosa_calder
    hide asha_patel

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: The motif holds—uplifting, forward-moving]
    # play sound "sfx_placeholder"  # [Sound: Murmurs of conversation, a harmonica line threading through]
    "You close your notebook for a moment and let the day's evidence sit in you: hands in soil, Theo's open data, Rosa's stories, Elias 'Eli' Maren's music, and a distant, complex gaze from Dr. Sienna Kade. Each element is a stitch."
    "Page-turn thought: You have sewn a demonstration that is impossible to reduce to a slide deck. It is living, muddy, and noisy—what you need it to be. The plan for tomorrow is already taut in your"
    "mind: amplify the demos, make the metrics public, feed the volunteers, and craft the public narrative so that when Dr. Sienna Kade and others come looking for a single lever to pull, they'll find something that"
    "can't be unhooked from people."

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
