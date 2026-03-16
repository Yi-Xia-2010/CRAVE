label chapter4:

    # [Scene: Moonlit Boardwalk | Night]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the soft hiss of water against pilings, muffled voices and the low hum of a small motor]
    # play music "music_placeholder"  # [Music: Gentle, rising strings with a steady rhythmic undercurrent—hopeful but careful]
    "You came because the choice you made in the last room pressed like a stone in your pocket. You chose to test, to put a prototype where your neighbors could see it—where the salt and the"
    "people and the memory all meet. Tonight, the boardwalk is a small, impossible stage: old rope, patched wood, the smell of diesel and brine braided with coffee and the sweet, tangy steam from Mira’s thermos."

    scene bg ch4_453e40_2 at full_bg
    "You set your field journal aside, its margins full of routes and names that have kept you awake for years. Now the margins share space with Ilan’s crisp schematics taped to a lantern post, paper corners damp with spray. Your fingers still smell faintly of ink and solder."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "Alright—snap here, then rotate. The gasket should seat before you torque it down. If it leaks, don't panic; that's fixable."
    show ava_marin at right:
        zoom 0.7

    ava_marin "How many degrees?"

    ilan_cortez "Twenty-eight, then a quarter-turn. Trust the gasket. Trust the people who made them.' (He glances at you, then deflects.) 'You taught me to test in the rain."
    "You laugh, because you did, once—standing in Tomas's shed while a storm tried to swallow the pier—and because it’s true. The laughter loosens someone’s shoulders nearby; hope, tonight, behaves like something mechanical you can calibrate."
    hide ilan_cortez
    hide ava_marin

    scene bg ch4_453e40_3 at full_bg
    show mira_soto at left:
        zoom 0.7

    mira_soto "Hot coffee! And—who wants extra rope? Tomas says we can tie the modules to the old cleats."
    show tomas_marin at right:
        zoom 0.7

    tomas_marin "Those cleats have kept our boats for forty years. Tie 'em good, or I'll shame you into retying them tomorrow."
    "You watch Tomas’s hands—oil-stained, steady—loop new rope through an old cleat. His ponytail is damp; his laugh is dry with salt and memory. He grips a line and tests a knot, teaching a teenager to finish"
    "it. These are the small trades that built Tideward; tonight they scaffold a new intention."

    menu:
        "Hand Ilan the torque wrench":
            "You slide the wrench into his palm. He nods, a grateful look passing across his face, and you feel your spine unbending a degree."
        "Call out the measurement from the diagrams":
            "You read the number loud—other hands echo it—and Ilan steadies, the joint clicking into place with collective effort."

    # --- merge ---
    "The crowd continues to work as the first module is adjusted."
    "The first module leaks like a nervous laugh. Water beads at a seam then runs cold across the plank. A ripple of amusement passes through the crowd—who else but Tideward would cheer when a thing fails"
    "and then is fixed? Someone—an old neighbor you haven't seen in months—claps and someone else offers a strip of spare gasket. You hand it over because habits of repair are habits of care."
    "Ilan Cortez: (runs a gloved hand along the seam, then tightens.) 'They can snap together, be taken apart. If a street needs a path, we make it a pathway. If a corner needs a garden, the"
    "modules go to the side. They're meant to be borrowed by the neighborhood, not owned by a corporation.'"
    show ava_marin at center:
        zoom 0.7

    ava_marin "They look solid. They feel—reparable."
    hide mira_soto
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "I wanted them to be... respectful. Fast to deploy, fast to return to other uses."
    "You study his face in the lanternlight—the determination, the worry folded into it. There is something tender in his optimism, as if he believes hope can be engineered and you are watching him solder it into place."
    # play music "music_placeholder"  # [Music: A warm swell; strings and a gentle woodwind flourish]
    # play sound "sfx_placeholder"  # [Sound: A soft click, then quiet applause; the hum of a microfilter kicking on—high, steady, promising]
    hide tomas_marin
    show rahim_okoye at right:
        zoom 0.7

    rahim_okoye "This wins hearts, Ava—and maybe a few headlines. People see something that protects them without telling them they have to leave."

    ava_marin "That’s the plan. Let it be something we can touch, not just a line on a map."

    rahim_okoye "Be careful. Municipal interest can convert community designs into municipal property fast. If a tech looks like a fix, it becomes a line item; if it becomes a line item, it becomes negotiable."

    ava_marin "Negotiable how?"

    rahim_okoye "Sometimes that means funding without conditions. Sometimes it means rules that allow private contractors to install 'improvements' and then charge for access. You know the history—developers have a habit of turning resilience into rent."
    "Ilan looks over at Rahim, then back at you. There's tension balanced with trust: Rahim has the breadth to see systems; Ilan builds devices within them. You understand both impulses, the engineer’s impulse to make tangible solutions and the advocate’s to guard the commons."

    ilan_cortez "What if—we document, and we copyright it, and—"

    rahim_okoye "Copyrighting won't stop appropriation. It will just change who profits."
    "You feel that old guilt, the one that collapses your shoulders until your ribs ache. But tonight something steadies it: hands that have known how to mend, voices that know how to debate without cleaving. People"
    "start to imagine staying in their houses not as a stubborn clinging but as a plan."

    menu:
        "Ask Rahim about a coalition route":
            "You turn to Rahim directly and ask about formal channels. He leans in and outlines a cautious pathway—petitions, public demonstrations, grant applications—each with its own trade."
        "Call for a vote among those present":
            "You raise your voice and ask the neighbors to decide. Voices rise and fall, small hands lifted in lamplight; the community’s agency hums like an instrument finding pitch."

    # --- merge ---
    "The community conversation continues, informing the group's next steps."
    "A press drone—small, discreet—hovers at the edge of the fog. Someone from a local paper says they’ll run a piece. The idea of the city noticing a grassroots demonstration is thrilling and dangerous, like lighting a signal fire that might be seen as a beacon or a target."
    "Mira Soto squeezes your shoulder with both hands. Her thermos is empty now, but her eyes are bright."
    hide ava_marin
    show mira_soto at center:
        zoom 0.7

    mira_soto "Imagine the kids seeing this and thinking staying was possible. Imagine the seed-exchange next to a barrier that keeps their school dry."
    hide ilan_cortez
    show ava_marin at left:
        zoom 0.7

    ava_marin "That’s the whole point. It's for the kids and for the old people who shouldn't have to leave their koi."
    "Tomas smiles—rough, private—but there’s pride in it. He picks up a small piece of scrap and fits it into a module as a brace. It’s improvisation, yes, but also lineage: Tideward fixes what it can, remembers what it must."
    "The night stretches. Scaffolds rise from salt and rust, microfilters pulse like a heartbeat, and for the first time in months you sleep without waking from your guilt. You lie in a cot tucked into Mira's"
    "van, the boardwalk layout in your head, the sound of the microfilter in a distant rhythm. Hope feels perilous and real—like a tide held back for a night by human hands."
    hide rahim_okoye
    hide mira_soto
    hide ava_marin

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Soft, ascending; light piano and warm strings]
    "By morning, Rahim is back, less spectator and more strategist. He walks the modules, kneels, tests a joint with the kind of clinical curiosity that has saved and muddled policies."
    show rahim_okoye at left:
        zoom 0.7

    rahim_okoye "If we want to scale this without losing governance, we need—documentation, legal framing, a coalition. I can help draft a petition that asks for municipal funding while listing community governance clauses."
    show ava_marin at right:
        zoom 0.7

    ava_marin "You mean a formal partnership—money but terms."

    rahim_okoye "Yes. It could keep this in neighborhood hands legally, but it will put you in a negotiation room with people who read numbers and rewrite narratives."
    "Ilan watches you watch Rahim. His jaw tightens—he understands the technician’s fear of bureaucracy: how red tape can calcify into something inert, how good intentions can be footnotes."
    show ilan_cortez at center:
        zoom 0.7

    ilan_cortez "We have to be careful that in trying to protect the design we don't make it untouchable."
    "You feel the pull between making technology free and protecting it from capture; between scaling what works and keeping your community’s autonomy. This is not a choice you make alone—your neighbors have already started to offer pieces of themselves to the work."
    # play music "music_placeholder"  # [Music: A decisive but gentle chord that lingers]
    "The boardwalk hums with new possibility. People who slept with the sound of the sea in their bones wake with a plan in their hands. You tuck a damp strand of hair behind your ear and"
    "trace the silver wave ring on your finger. The ring fits like an anchor; tonight it steadies your resolve."
    "There is momentum. There are risks. There is a new, collective muscle learning how to flex. The choice ahead will determine not only the fate of a piece of hardware, but the shape of who you become in Tideward's story."

    menu:
        "Document and open-source the design widely to protect it from appropriation.":
            jump chapter5
        "Formally collaborate with Rahim to petition municipal funding while protecting community governance.":
            jump chapter6
        "Keep the pilot local and stealth—scale only by word-of-mouth.":
            jump chapter11
    return
