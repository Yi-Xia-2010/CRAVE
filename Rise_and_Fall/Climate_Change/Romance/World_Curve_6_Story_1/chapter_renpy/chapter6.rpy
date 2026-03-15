label chapter6:

    # [Scene: Rahim's Office | Late Afternoon]

    scene bg ch6_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scratch of a pen, distant gulls, the low rumble of a truck on wet cobbles]
    # play music "music_placeholder"  # [Music: Low, warm amber synth—a chord that doesn't fully resolve]
    "You sit at Rahim's scarred table, the agreement folded in front of you like a small, heavy tide. The ink on the pages smells faintly of copier toner and old coffee. Your pen feels oddly ceremonial in your hand—an offering to a future that somehow fits inside a clause."
    "Rahim leans forward, palms flat on the paper. His voice is steady, the way he sounds when he moves between neighborhoods and the city hall bureaucracy like a translator."
    show rahim_okoye at left:
        zoom 0.7

    rahim_okoye "Community oversight, rotating control panels, guaranteed seats on the maintenance board—those are non-negotiable from our side. We tie them to the funding lines; we tie them to audit windows."
    show ava_marin at right:
        zoom 0.7

    ava_marin "And the audits—who runs them? Who looks when a clause gets reworded by lawyers who don't know the names of our streets?"

    rahim_okoye "That's why we put in language for community auditors and a rotating third-party review. Not ideal, but transparent. We try to make the terms sting as little as possible."
    "Ilan Cortez sits to your left, sleeves rolled, a smear of printer ink along his forearm. He taps a schematic on his tablet and then looks up, amber eyes finding you in the dim light."
    show ilan_cortez at center:
        zoom 0.7

    ilan_cortez "Fail-safes are mechanical and social. If a private contractor misses maintenance, the co-op's override kicks in. If the sensors fail, manual ballast protocols work with what Tomas's boats can handle for short periods. We designed redundancy around local knowledge."
    "You watch him explain, and your chest tightens in a way that's animal and honest—you want to believe him, because you want the neighborhood to breathe. You also remember every time a new machine promised safety and left a hole where people used to stand."
    "Rahim slides a page across to you. The clause about 'performance targets tied to release schedules' is boxed in small font. You feel its presence under your fingertips like an undertow."

    menu:
        "Press the pen to the paper and sign as-is":
            "You press the pen down, feeling the nib scratch your name into law. The room shifts slightly—agreement made, responsibility accepted. Rahim exhales, clearly relieved. Ilan's fingers find yours for a moment, a quiet acknowledgement of the pact."
        "Fold the paper back and ask Rahim to read the boxed clause aloud again":
            "You fold the page and make Rahim read the boxed paragraph line by line. His voice tightens at the 'maintenance contracts' section, and you feel the room hollow with the weight of possibility. Ilan grows quiet; his jaw sets. The signing is delayed, but the terms are clearer, and that delay feels like buying time rather than surrendering it."

    # --- merge ---
    "Continue with Rahim's response below"

    rahim_okoye "Delays cost leverage sometimes. But transparency costs less than regret. If you want the wording changed, we'll change it. There are avenues."

    ava_marin "You sign. You do not sign without thinking; you sign because people have already been waiting on more than paper. Your name folds into the ledger of the city in a way that will smell faintly of salt and compromise."
    # [Scene: Tideward Boardwalk | Weeks Later | Golden Hour]
    hide rahim_okoye
    hide ava_marin
    hide ilan_cortez

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The quick, rhythmic thrum of pumps; small children laughing in the distance; the low murmur of people trading parts]
    # play music "music_placeholder"  # [Music: A pragmatic, hopeful piano motif that carries a thin tension underneath]

    "For a few months, the ledger looks balanced. Tidal alerts ping into a community co-op platform you helped set up—messages full of practical things" "Barrier 3 shifted. Manual ballast required. Tomas available at 1700."
    "Mira presses a thermos into your hands, eyes crinkled with something like triumph."
    show mira_soto at left:
        zoom 0.7

    mira_soto "You should've seen Roo's face when we rerouted the alerts to the co-op. She said it felt like the town crier came back."
    show ava_marin at right:
        zoom 0.7

    ava_marin "We did it together. Everybody pulled."
    "Tomas arrives with oil-scented hands and a grin that doesn't quite reach his eyes. He pats a barrier with the fondness of someone who understands the stubbornness of machines and the stubbornness of people."
    show tomas_marin at center:
        zoom 0.7

    tomas_marin "They're holding for now. But you know how water is. It pushes and pushes until you learn to move with it, not only against it."
    "You nod. You have been moving with it—through meetings, through nights spent sketching redundancy protocols in the margins of your journal, through small triumphs that taste like solder and sweet tea."

    menu:
        "Crowd-surf the momentum—lead a public 'thank you' at the community square":
            "You step onto a crate and speak about the work—about hands, not ledgers. People clap, a warm, human sound that steadies your throat. Ilan watches you from the edge, pride and impatience kindling behind his eyes."
        "Slip away with your journal and record stories of the old street names instead":
            "You tuck yourself behind a stacked pallet and open your journal. You write the names people call the alleys—small resistances that keep memory from dissolving into municipal charts. You breathe easier, but you also feel distant from the movement you helped steer."

    # --- merge ---
    "Continue with the account of municipal language shifting below"
    "The downbeat returns in small ways. City Hall begins to adopt the language you fought to keep out—now reframed as 'efficiency savings' in Evelyn Harrow's speeches. At a municipal press event, she stands in front of"
    "a glass railing, rain-trimmed suit immaculate, the city's tidal metrics ticking on a lapel display."
    hide mira_soto
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "Our partnership with neighborhood co-ops provides resilience at lower cost. The modular systems proved effective in pilot zones. With performance-based funding, we ensure taxpayer dollars produce measurable outcomes."
    "You watch her wordsmith livelihoods into spreadsheets. Her tone is methodical, the cadence of someone who has learned to convert grief into policy that sounds inevitable."
    "You—listening—feel language retracting the edges of a place into numbers."
    # [Scene: City Hall Promenade | Rain-slick Morning]
    hide ava_marin
    hide tomas_marin
    hide evelyn_harrow

    scene bg ch6_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A camera shutter; umbrellas rustling; a distant wave hitting a revetment]
    # play music "music_placeholder"  # [Music: A cool, clinical string line underscoring the crowd's murmurs]
    "You stand with a cluster from Tideward—faces you've seen in kitchens, on roofs, under open skies. Rahim is there too, a stable presence. Ilan Cortez's hand brushes yours and is gone, his posture tighter."
    "A neighbor from the co-op board—someone you've seen at repair nights—approaches you, jaw working."

    "Neighbor" "They're offering Samuel a consulting slot. He hasn't said yet. They told him it'd 'ensure continuity'—and a stipend that could help him keep his place. But they want a non-disclosure."
    "Something in your chest drops, metal on salt. A consulting job becomes a silence-in-contract. A stipend becomes a quiet closing of a door."
    show ava_marin at left:
        zoom 0.7

    ava_marin "We built this to keep people here, not to have them buy quiet with their names."

    "Neighbor" "He's tempted. Who wouldn't be?"
    show ilan_cortez at right:
        zoom 0.7

    ilan_cortez "We need to make sure offers like that don't undermine the co-op. If someone takes private money, the maintenance contracts shift. That's how pieces get carved away."
    "You try to explain the ledger in ways that aren't spreadsheets—you point to recipes Mira has cataloged, to the corner where a children’s game used to mark the end of the street—but language frays when legal forms arrive."

    menu:
        "Stand up and demand the co-op publish every offer transparently":
            "You step forward, voice steady through the drizzle, and demand transparency. The crowd turns. There is a shiver of solidarity; some hands go to phones. Rahim catches your eye and nods—he's already drafting a public registry."
        "Pull aside Samuel and ask about his reasons before calling him out":
            "You find Samuel behind a column and ask him quietly why he'd consider it. His voice trembles—fear mixed with exhaustion. He has a mortgage that keeps dry the home his mother once owned. You understand the ledger in a way that tightens your throat; you don't call him out, because his choice isn't only his."

    # --- merge ---
    "Continue with the Saltworks Lab scene below"
    "Back at the Saltworks Lab one night, Ilan Cortez and you stare at a wall of schematics. He traces a deployment map with a finger, eyes bright with plans that could scale beyond your shore."

    ilan_cortez "If we replicate this in other neighborhoods, we outpace the contracts. We prove a decentralized model works at scale, and then policy adapts."

    ava_marin "And if scale attracts corporate partners who want to patent what we built? If 'scale' becomes an invitation to extract?"

    ilan_cortez "We can license it on terms that keep it open. We can—"

    ava_marin "You cut him off, not to stop the sentence but because stopping feels easier than the list of ways intentions go soft."

    ava_marin "Terms are paper. People are the ones who keep the place alive. My journal is full of songs and eulogies and routes—things a model can't measure. How do you make a spreadsheet care for a recipe?"

    ilan_cortez "You always loved lists more than blueprints."

    ava_marin "I loved people more than budgets."
    "His silence is not a refusal but a bruise. For all his patience with bolts and circuit boards, he becomes impatient with the social scaffolding—he thinks in iterations and deployments, and the slow churn of meetings feels like sand in his gears."
    # [Scene: Tideward Rooftop | Dusk]
    hide ava_marin
    hide ilan_cortez

    scene bg ch6_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation; the clink of cups; the distant beat of a radio playing an old dance tune]
    # play music "music_placeholder"  # [Music: A melancholic guitar riff underlaid with the timbre of a single, held cello note]
    "There is a small celebration—subsidized beets, a patched banner that reads 'Tideward: We Remember.' You hold your journal on your lap. Pages are filling faster than you can archive them. There are recipes, names of alleys,"
    "a map of where the milkman left his crate—tiny resistances that insist on being counted."
    "Someone raises a toast to 'engineering and community,' and you lift your cup because the work has kept roofs over heads. It tastes of metal and salt and something like relief."
    "But underneath the cheer is the quiet of small betrayals—a neighbor's consulting offer, an unsigned maintenance contract, a target that calls for efficiency over ritual. The co-op's meetings now include municipal liaisons in suits who talk about 'metrics' as a secular sermon. Your journal’s margins are crowded with elegies."
    "Tomas finds you, his hands smelling of oil and salt."
    show tomas_marin at left:
        zoom 0.7

    tomas_marin "You did good. You saved roofs for people who would have left otherwise. Don't forget that."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Saved some roofs, Tomas. But how many names do we sell to keep one roof up?"
    "He looks at you like the ocean looks at the shore—patient, a little weathered, not offering a tidy answer."
    # [Scene: Moonlit Boardwalk | Night]
    hide tomas_marin
    hide ava_marin

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft slap of water; your notebook's pages rustling in the wind]
    # play music "music_placeholder"  # [Music: Sparse, descending strings—an ache without resolution]
    "You walk the boardwalk alone. The modular barriers stand like faint ribs against the moonlit water. The city feels both safer and thinner—less a neighborhood, more a calculation."
    "You open your journal. The pen moves slow. You write the names you promised to keep. You copy recipes, scrape together small histories, sketch faces you've seen for years. The act of writing is a kind of reclamation."
    "Ilan Cortez joins you without fanfare. He doesn't speak at first; he stands close enough for the warmth of his breath to mix with yours."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "I thought the ledger would be a small thing to bear—that we could measure and then protect. But the ledger keeps expanding."
    show ava_marin at right:
        zoom 0.7

    ava_marin "It's not just numbers for me. It's names, Tomas's way of cursing the tide when a line snaps, Mira's seed packs with their handwritten notes. Those don't fit into 'efficiency savings.'"

    ilan_cortez "What do we do with that? How do we keep those things from being footnotes?"
    "You both look at the water. It moves indifferent to human accounting."

    ava_marin "We keep doing it. We keep naming. We keep building redundancy—in steel and in story. Maybe it's not enough to make the city friendly, but it keeps us honest."
    "He reaches for your hand. His fingers are warm and rough from work, ink on his skin."

    ilan_cortez "I'm tired. I'm tired of designing only to watch people make choices I'm not prepared for. I'm tired of the way the city turns a people's project into a contract."

    ava_marin "So am I."
    "There is no dramatic falling out. There is only the slow, inevitable wearing of things against one another. Your hands find each other like two tools that still fit in the same grip. Love is present, tender and frayed."
    "You close the journal and slide your pen into the loop on its cover. Outside, somewhere in the neighborhood, someone is singing a song that your grandmother used to hum while mending nets. The melody is small and stubborn; it refuses to be parceled into policy."
    "You let the melody fill the hollow left by clauses and metrics for a minute, a balm that costs nothing on any ledger."
    "You have helped keep people housed. You have invited the city into your workshops to try to preserve that housing. You have seen the cracks where money and prestige pry at the seams. You have watched"
    "a neighbor consider selling their silence for survival. You have loved someone who measures the world in prototypes and deployment maps."
    "It is a satisfactory kind of success in one register and a quiet betrayal in another."
    "You stand there in the moonlight, tasting the salt and the small, bitter sweetness of compromise. You do not have a clear victory to write into the margins. Instead, you have work to keep doing—making redundancy"
    "for bodies and for stories, stitching policy to practice where you can, remembering the recipes and alley-names even as the city recalibrates its priorities."
    "You fold the journal into your jacket and walk back through the wet lane. The LED indicators on the barriers blink green—machines fulfilled their role tonight. The people who use those streets breathe again for now."
    "You keep walking because movement is a promise, even an imperfect one."
    hide ilan_cortez
    hide ava_marin

    scene bg ch6_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, falling piano chord, then a quiet hum]

    scene bg ch6_4001e7_7 at full_bg
    "THE END"
    # [GAME END]
    return
