label chapter4:

    # [Scene: Dunes and Emergency Barricade | Late Afternoon]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent drum under a children's chorus — a protest hymn half-remembered]
    # play sound "sfx_placeholder"  # [Sound: Gulls raking the air; the distant, regular slap of tide against dune; voices carrying over wind]
    "Narration:"
    "You chose this. You remember saying yes not because it would be easy, but because Elias Novak's urgency matched the ache in your chest — the same ache that pulled at the red thread around your"
    "wrist. Now his sandy hair is damp, the film camera at his throat like a talisman that keeps him steady. He moves through the crowd the way light moves through water: scattering, gathering, always in motion."
    "Narration:"
    "You are elbow-deep in salt and paint. Your hands smell of tar and marker ink; sand has worked into the old cuff of your jacket and into the small scars on your palms. The barricade is"
    "a patchwork: donated pallets, thrift-store ladders, rope, and sandbags sewn together by neighbor hands. Someone has added bright cloth pennants with slogans in shaky script: KEEP SALTBRIDGE HOME, HANDS NOT WALLET, RAISE THE PEOPLE NOT JUST"
    "THE WALL."
    "Narration:"
    "Rosa's voice threads through the noise as she passes by with a flying tray of pastries, steam making halos in the air. Finn hauls a ladder into place, mud streaked across his forearms, jaw tight but"
    "steady. There is a warmth under the damp — the old small-town cohesion like a familiar coat thrown over your shoulders. For a moment the weight of the plan thins; a child's chant loops and you"
    "almost sing along."
    show elias_novak at left:
        zoom 0.7

    elias_novak "Okay, Maya — banner here. We need a photo from the line, from low. It'll show we blocked access, make it harder to spin."
    "Narration:"
    "He grins, camera already up, but the grin doesn't reach his eyes."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Low and tight,' you say, breath fogging. 'But don't get on the wet slope. Finn — tie that line further down, the bags slip there."
    show finn_serrano at center:
        zoom 0.7

    finn_serrano "On it."
    "Narration:"
    "He takes the rope with a grunt, the ladder clanking under his palm. 'If the tide pops, it'll be at the seam near the old driftwood. We should double up.'"

    elias_novak "We'll double up. We'll sing. We'll hold the line."
    "Narration:"
    "You give the order because people look to you to turn intention into action. You find your voice in the small things: who ties where, which gaps to stuff with extra burlap. Everything is tactile —"
    "the scrape of twine, the damp slap of sandbags, the metallic taste of your own nerves at the back of your throat. The camera clicks — Elias Novak records, exuberant and raw — and the moment"
    "feels both revolutionary and fragile."

    menu:
        "Tie the banner yourself":
            "You take the banner's edge, your fingers catching on the damp fibers. Your hands move on practiced knots; you feel less like a leader and more like someone patching a wound. Elias Novak shoots a candid and laughs — a bright sound — then helps tuck the corner."
        "Send Finn to tie it while you check the seam":
            "You hand the rope to Finn and walk the line, eyes combing for weak spots. Your heart skips when you find a small subsidence near an old pallet; you jam a spare bag into the gap and whisper a promise to the town you almost can't afford to make."

    menu:
        "Call for medics to be on standby":
            "You lift your voice and shout for medics; someone with a raincoat and a first-aid kit steps forward. Their arrival steadies the group like a tether."
        "Keep the group focused on visibility — block the road longer":
            "You urge people forward, closer to the edge of the access. The press leans in. Elias Novak catches your shoulder, a question in his look; you say nothing, unable to tell him that the seam in your chest is widening."

    menu:
        "Tell Elias Novak you're ready to escalate":
            "You meet his eyes and say the words. His face opens like a sun. He squeezes your hand, already sketching a plan out loud; the tide of volunteers looks hungry and ready."
        "Ask Dr. Hana for a pause to gather evidence":
            "You turn to Dr. Hana and nod. She pulls up tide data on her tablet and shows you a gap in the modeling — a way to frame the breach as preventable. There's relief in the math, but it tastes of delay."

    menu:
        "Double down on direct action with Elias — escalate to larger civil disobedience.":
            jump chapter5
        "Consolidate and rebuild community capacity — shift focus to mutual aid and Rooftop Sanctuary efforts.":
            jump chapter6
        "Request scientific backing from Dr. Hana to bring evidence to the Mayor.":
            jump chapter6
    return
