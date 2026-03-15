label chapter3:

    # [Scene: Old Ferry Mural | Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant gull, kids' muffled laughter in the alley, the persistent thud of a generator somewhere down the block.]
    # play music "music_placeholder"  # [Music: Low, uneasy cello underscoring the murmuring crowd]
    "You find the notice before you see all the faces. It is pinned to the lamppost nearest the mural with a municipal adhesive strip that still smells faintly of ozone and printer ink. The paper is"
    "crisp and legal in tone; Evelyn’s digital lapel metrics glow inside a laminated QR strip at the bottom as if the city itself has signed the sentence."
    "You stand with your silver wave ring warm against your finger, the salt crusting the metal like sedimented memory. The lamppost's light puddles over the notice and paints the edges of your jacket in halogen white."
    "Your journal is in your bag, the corner damp from the evening air, as if the city’s breath got into everything."
    "Mira is at your left, seed packets clutched to her chest like small talismans. Tomas is on your right, leaning hard on a wooden cane that smells of oil and old tar; he keeps saying words"
    "that are mostly curses and regret. Rahim paces a slow, deliberate ring around the crowd; his calm carries a pressure that settles in your ribs. People press in—neighbors with lanterns, a kid with salt in her"
    "hair, elders wrapped in blankets—faces made by weather and stubbornness."
    "You want to tear the paper down on principle, to rip the sentence out of the lamp’s post and hand it to Tomas so he can shred it into a dozen pieces. You want to read"
    "it aloud while your voice is loud enough to pull the horizon toward you. But the paper exists, and it is civically stamped. It is proof."
    "You touch the edge of the notice with a thumb gone numb from the cold. The letters are bureaucratic: “Managed Redevelopment,” “Consolidation,” “Resettlement Pathways.” There is a neat paragraph about compensatory infrastructure—renderings, charts, a municipal promise. Your throat tightens, and you taste the metallic tang of anger."

    menu:
        "Peel the notice down and hand it to Tomas":
            "Your fingers lift the edge and the strip tears with a dry sound. Tomas looks like he might smile and then doesn't; he folds the paper into his palm like a used map."
        "Read the notice aloud to the crowd":
            "You clear your throat and read the words slowly. The formal terms land in the air like small stones. A woman near the back starts to cry; Mira grips your sleeve harder."

    # --- merge ---
    "The crowd reacts; the meeting moves toward the community center."
    # [Scene: Community Center — Main Hall | Immediately after]

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chairs scraping, whispered arguments, the low hum of a projection unit.]
    # play music "music_placeholder"  # [Music: Sparse piano, a minor key that refuses resolution]
    "You step inside behind the crowd, the smell of boiled coffee and damp wool filling the room. The projection shows two different visions side by side: one is Evelyn's crisp renderings—sleek blocks on a raised boulevard,"
    "clear water channels, graphs that promise stability. The other is a sketchy collage of Tideward-made solutions—rope, pallets, solar panels, hand-lettered timelines. The images do not fit together."
    "Ilan Cortez is already there. He speaks softly when he speaks, hands moving like he’s sketching in the air. He lays out his plan in pieces that could be carried—modular barriers that click together, mobile filters"
    "that fit into a backpack, a training schedule that imagines neighbors building in shifts so no single household bears the whole labor. He calls it 'community-scaled tech.' His amber eyes are bright with the same careful"
    "hope that has followed him into every prototype."
    "You watch him, and a part of you relaxes because his voice is the kind you could follow into a workshop. Another part of you remembers the word 'co-option' and how well-sounding prototypes can be repackaged into policy that demands conformity."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "We designed the clamps so anyone can bolt them on. No heavy machinery. No expensive permits at the start. We teach three households one night a week—by the end of the month, the pier's cleared, and we have a working reef baseline."
    show ava_marin at right:
        zoom 0.7

    ava_marin "And the municipality? Rahim said—"
    show rahim_okoye at center:
        zoom 0.7

    rahim_okoye "Scaling these will require coordination. Logistics, supply chains, liability clearance. If we work with partners, the work moves faster, but oversight follows. We've seen how fast 'partnership' can become policy with strings."

    ilan_cortez "I know. The point is to keep control local. We can build a governance agreement—"

    ava_marin "Can you promise that the tech will remain ours and not turn into a condition for relocation?"
    "Ilan Cortez pauses. His jaw works. You see the prototype of something like regret cross his face, the brief darkening that happens when someone measures trade-offs as if on a scale."

    ilan_cortez "I can't promise municipal hands won't want in. I can promise to keep the designs open-source, to use local materials. But promises only work if we build the conditions to enforce them."
    hide ilan_cortez
    show mira_soto at left:
        zoom 0.7

    mira_soto "This could give us breathing room. We can teach kids—make it a summer thing. Tomas—"
    hide ava_marin
    show tomas_marin at right:
        zoom 0.7

    tomas_marin "Teach 'em to bolt on the banks while the city erases the streetnames? I fixed boats with my father. We don't need gismos that make a developer's render prettier."
    "The hall breaks into competing murmurs. Some hands raise for practical questions—who pays for materials, who teaches? Others shout about identity and memory—about the stories that will be lost if foundations are moved. The meeting feels like a muscle in spasm; every decision flexes different pain."

    menu:
        "Ask Ilan to show the prototype video now":
            "You ask him and he nods quickly, pulling up footage on his battered smartwatch. The room leans in; the hum of attention feels like a tide rolling back briefly."
        "Calm the room and push for a vote on a moratorium":
            "You raise your hands and speak to the crowd. For a moment the noise compresses into silence. People look to you—expectation, exhaustion, hunger."

    # --- merge ---
    "The meeting's focus shifts depending on your intervention; discussion continues into the night."
    # [Scene: Community Center — Later | Night]
    hide rahim_okoye
    hide mira_soto
    hide tomas_marin

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The click of a tablet, polite applause like a distant wave; someone mutters under their breath.]
    # play music "music_placeholder"  # [Music: A low brass line that makes the room feel official and small]

    "Evelyn Harrow speaks with the practiced cadence of someone who has convinced committees and committees of committees. Her words are tidy" "managed retreat,' 'strategic consolidation,' 'infrastructure investment."
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "We are offering relocation packages, prioritized infrastructure, a plan that stabilizes the whole borough. I know change is painful. I know it costs more than budgets allow. We will work with communities on phased transitions."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Phased for who? Phased at what cost? Phased for which memories?"
    "Evelyn Harrow's face shifts—something complex, not simply cold. Her eyes narrow for a breath, then settle in a way you cannot read clearly. The problem-check rule kicks in and you read her expression as unreadable; it fits whether she means consolation or calculation. It fits both."

    evelyn_harrow "The cultural cost is regrettable but measurable. Our obligation is to act at the scale the data demands. We cannot allow neighborhoods to become permanent liabilities. The city's fiscal capacity is finite."
    show rahim_okoye at center:
        zoom 0.7

    rahim_okoye "Data doesn't hold hands. It doesn't remember names. We need legally binding guarantees—cultural relocation funding, detached titles for preserved homes—before we discuss moving anyone."

    "A woman at the back lifts her voice, edged with something like grief and something like accusation" "You mean move us so your highway looks tidy. You mean fence us in 'safer zones' and call it care."

    evelyn_harrow "No—"

    ava_marin "Stop saying 'no' like a blanket. Tell us specifics. How is your plan keeping our networks—our gardeners, our elders, our night-watchers—intact? Or is it smoothing them away?"
    "Evelyn Harrow's reply is a list of clauses and contingencies that sound like a catalogue of compromise. She cites budget lines, donor constraints, and the temporality of grants. Her shoulders are squared against the room as if bracing to be the executioner and the surgeon at once."
    hide evelyn_harrow
    show tomas_marin at left:
        zoom 0.7

    tomas_marin "You can't sell bone with a smile, Evelyn. We built this place. You don't get to price its bones."
    hide ava_marin
    show evelyn_harrow at right:
        zoom 0.7

    evelyn_harrow "I know how that feels. My family lost land once. I—"
    "Her hand is quick to her tablet; she swipes something and the wall shows a model of possible new neighborhoods, compact and efficient. The room sees the possibility and the erasure simultaneously. The air becomes thicker, like the weight before a storm."

    menu:
        "Step in front of Evelyn and demand a public, recorded commitment":
            "You stand up, shoulders squared. People quiet because your voice has been used to call the neighborhood to action before."
        "Pull Ilan aside and ask if the tech could be adapted for mobilization without municipal approval":
            "You lower your voice and Ilan meets you halfway. He shows you a small schematic on his watch, fingers trembling with the same fear you feel."

    # --- merge ---
    "Tension intensifies; decisions about next steps solidify into plans and promises."
    "You feel the guilt that has sat under everything—since the storm that took half a block when you were sixteen, since the patchwork repairs, since every choice that might have moved someone. It presses into your"
    "chest like a tide that will not obey sandbags. Each possible next move presses on that same vulnerable point."
    "Rahim folds his arms and looks at you, an offer and a challenge in equal measure. Mira watches you with seeds still clutched as if she expects you to pick which ones to plant and which"
    "to save. Tomas is numb and furious in equal parts. Ilan Cortez's gaze holds a question that has nothing to do with kits and everything to do with whether you believe people can be entrusted with"
    "decisions."
    "Your voice is the one they look to—it always has been in small, trembling ways. You could steer them toward hands-on building. You could steer them toward legal resistance. You could steer them toward a direct confrontation that forces the city's hand."
    "You inhale the brine-sweet air, taste metal and coffee and wet paper. You remember the map in your journal and every route you vowed to protect. You remember the slow ember of resolve that guided you"
    "here, and you know that tonight will define what being a leader in Tideward will mean when the city's machines arrive."
    "Your chest tightens with the old guilt and the new pressure; you feel the tide of the room pressing against your ribs. There is no neutral place to stand. The meeting fractures into side conversations again—someone"
    "threatens legal action, someone else offers to mend a prototype now. The momentum splits like light through a prism. Your hand hovers above the table as if over a scale."
    "You breathe and choose how to speak."
    hide rahim_okoye
    hide tomas_marin
    hide evelyn_harrow

    scene bg ch3_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: A single minor chord held, unresolved]
    "You step forward."
    show ava_marin at left:
        zoom 0.7

    ava_marin "Listen—this is not about one plan being better. It's about who gets to decide how we live. We can build, we can litigate, we can demand transparency. But first we need to pick how we will lead tonight."
    "You look at Ilan Cortez. You look at Rahim. You look at Mira and Tomas and the faces of Tideward folded into jackets and blankets."
    "The room waits."

    menu:
        "We pilot Ilan's modular tech on the old boardwalk with the community.":
            jump chapter4
        "We mobilize a legal stay and push for community-led planning only.":
            jump chapter7
        "I go straight to City Hall to confront Evelyn and demand transparency.":
            jump chapter10
    return
