label chapter17:

    # [Scene: Moving Trucks | Dawn]

    scene bg ch14_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hopeful piano pattern; gull cry sampled into the rhythm]
    # play sound "sfx_placeholder"  # [Sound: Engine idles, rope creak, distant hammering]
    "You wake before the sun, because old habits are a kind of muscle memory. Your tide-watch is cool under the blanket of your wrist, its brass face flecked with salt and hospital bleach and the scuff"
    "marks of a thousand small urgencies. The town smells like itself—sea-slick wood, diesel, the faint yeast-sweet warmth from the bakery—and the scent makes your chest tighten in a way that is both grief and vow."
    "You move through a short, precise ritual: fold the last of the seed-bank manifests into a plastic sleeve, run your thumb along the crate label where Rita's handwriting curls, tuck the faded festival patch Elias Jun"
    "insisted on keeping into a zipped pocket 'for luck.' Your fingers catch on a splinter in the packing crate; it stings, and you smile anyway because odd little pains are proof you are still here, doing"
    "the thing."
    "Elias Jun is already at the back of Truck Two, kneeling in a spill of shadow and dawn. He hands you a crate wrapped in tarpaulin with a grin that dangles between stubbornness and something softer. His palms leave dark smudges on your forearms when he passes you the strap."
    show elias_jun at left:
        zoom 0.7

    elias_jun "You sure you want to carry the tomato grafts? You'll grieve the loss of Marisora one bite at a time if you don't keep cultivating something familiar."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "If I don't bring them, someone else will. Besides—' (you force a lightness you don't entirely feel) '—we'll grow new recipes upriver. Maybe graft a memory into the soil."
    "Elias Jun rubs his thumb over the crate's label as if blessing it."

    elias_jun "We can build this. All of us together. Rita's got the manifests, Arlo's on water filters, and Dr. Ayla Voss—' (he pauses when he says her name, searching your face) '—Dr. Ayla Voss did the red tape. She's… doing the thing she does."

    maya_reyes "She's doing the thing she thinks will save us."
    "Elias Jun nods slowly. His jaw works as if chewing on the weight of that sentence, then he brushes at the side of his face with the back of his hand as if to sweep doubts away."
    hide elias_jun
    hide maya_reyes

    scene bg ch14_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of generators; someone nearby cusses cheerfully while dropping a wrench]
    "Rita Ortega arrives in a flurry of color—apron streaked with soil, keys jangling like a small orchestra. She moves between you and Elias Jun as if sweeping between two flames that need to stay apart but not extinguished."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "You two arguing already? Save it for the road. Here—' (she presses a thermos into Maya Reyes's hands) '—for the trip. And Maya?' (her voice softens) 'Remember—letters and seedlings. Don't wait."
    "You swallow the thermos heat and the hollow it fills. Your throat is a knot of vows you haven't yet said aloud."

    menu:
        "Tuck a strip of the harbor's weathered rope into your kit":
            "You twist the frayed rope between your fingers, the salt grit grounding you. When nights get thin, you know you'll hold that texture and remember the harbor's geometry."
        "Slip Rita's apron scrap into your pocket":
            "The scrap smells faintly of compost and jubilation. You press it to your nose at the first rest stop and the smell steadies your breath."

    # --- merge ---
    "Narrative resumes as the convoy departs upriver."
    # [Scene: On the Road | Midday]
    hide rita_ortega

    scene bg ch14_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Steady acoustic guitar with a rising cello]
    # play sound "sfx_placeholder"  # [Sound: Tires on wet pavement; tinny radio broadcasting a community station in the background]
    "The road carves a new horizon. The convoy moves like a slow migration: a careful, coordinated exodus. Inside the truck, the air is a brine-and-cardboard mixture—old seed packets, fuel, the faint perfume of Elias Jun’s sawdust."
    "You sit on a crate, knees bruised from a hundred municipal meetings, watching the river bend. You imagine the houses of Marisora—crooked porches, the bakery's crooked neon, the harbor's steady sigh—sliding past like frames in a"
    "film you are no longer allowed to linger in."
    "Elias Jun leans his head back against the metal skin and stares at the roof as if reading a sky he knows how to translate."
    show elias_jun at left:
        zoom 0.7

    elias_jun "Do you ever think about how it's the little rituals that keep us anchored? The way my dad used to tie nets—he had a rhythm. If you lose rhythm, you lose so much."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I think about rhythm all the time. Data is rhythm, too—tides, temperature, resource cadence. We translate it into models and plans and sometimes—' (you search for the phrase that will be true but not cruel) '—we translate it into leaving."
    "His hand finds yours across the crate. For a beat it's an ordinary weathered grip, then it becomes declaration."

    elias_jun "We promised we'd write. We'll keep the rhythms alive, even on opposite schedules. We'll stitch new ones."

    maya_reyes "Stitching is a good verb for what we'll do. It's slow. It takes hands."

    elias_jun "You're full of technocratic metaphors today."
    "You both laugh, the sound like a small buoy in a wide current."
    # play sound "sfx_placeholder"  # [Sound: A small, delighted chorus as Arlo Benitez bursts in with a clanking water-filter prototype]
    show arlo_benitez at center:
        zoom 0.7

    arlo_benitez "Look! It works—sort of. We have bubbles!"
    hide elias_jun
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "Of course it works. If it didn't, it wouldn't be Arlo."
    "Dialogue expands—Arlo asks practicality questions about setup, Rita negotiates housing allocations, Elias Jun keeps steering the conversation toward scaffolding and community kitchens. You answer in the language you know best: logistics, timelines, and the soft, human details—who sleeps where, who can cook, which seed varieties can survive the upriver salinity."

    rita_ortega "We need more hands on greenhouses. Maya, can you teach a workshop?"

    maya_reyes "Yes. And I'll map out the modular aquaculture layout this week. We'll stagger the builds so people can keep working and tending their plants."
    "Elias Jun squeezes your hand again, an agreement dressed as a small touch."

    menu:
        "Open the manifest and double-check the seed varieties":
            "The manifest is a small litany. You trace the names—sweet basil, red currant tomato, mangrove seedlings—each a promise that what you saved will grow again. The clarity steadies you."
        "Close your eyes and listen to the river instead":
            "You let the river's shape outline your breath. In that quiet you hear your own intentions clearer than a list—what you want to carry, what you want to leave."

    # --- merge ---
    "The convoy arrives at the new town and the group begins to organize the temporary quarters."
    # [Scene: New Coastal Town - Temporary Quarters | Dusk]
    hide maya_reyes
    hide arlo_benitez
    hide rita_ortega

    scene bg ch14_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings and light percussion; a rising minor third resolving into open fifths]
    # play sound "sfx_placeholder"  # [Sound: Soft chatter, the clink of pots and soil, a distant gull]
    "You step off the truck and into a town that is equal parts stranger and comfortable cousin. The planners' choice put you upriver: less storm-swept coast, a broader estuary, new possibilities. The air tastes less like"
    "brine and more like river algae and citrus from a vendor's stall. The temporary quarters are modest—rented rooms stacked into a building retrofitted with communal laundry lines and a rooftop that can hold a few crates"
    "of soil."
    "Elias Jun and you haul the seed banks up a narrow metal stair, shoulder to shoulder. Your palms ache exactly the right kind of honest ache. You remember the hospital's fluorescent lights and the ledger in"
    "your lap, and you find that the ledger is lighter now for having been used—the signatures are a record of choice, not defeat."
    "Inside, people move like a careful family. Rita Ortega immediately commandeers the kitchen, laying out a plan for communal meals. Dr. Ayla Voss appears, her trench coat buttoned and her satchel heavy with both maps and"
    "something softer—maybe an offer of technical support. She nods at you when she sees you and for a moment her expression is complex and unreadable—no accusation, no effusive praise, only the unmoored weight of someone who"
    "has made hard choices."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "You've done the hard work of carrying more than boxes, Maya."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We carried what we could. We left what we couldn't."

    dr_ayla_voss "And you must learn to make peace with what that means. For the people you left and for yourself."

    maya_reyes "Peace is a long project."
    "Her mouth tightens. She hands you a small, folded brief—administrative support, tax credits for community agriculture. It is practical; it is something to build with."
    show rita_ortega at center:
        zoom 0.7

    rita_ortega "Right now—plants. Forever household chores later. Maya, will you start with the greenhouse foundation?"

    maya_reyes "I'll supervise. Elias Jun can order the modular frames."
    hide dr_ayla_voss
    show elias_jun at left:
        zoom 0.7

    elias_jun "I can fabricate them in my sleep at this point."
    "You both grin, and the ease between you blooms a little. There are practical constraints—no one believes the first month will be idyllic—but there is also a clear, rising momentum. People who had been adrift are"
    "finding a place in the new work, and each task they take on mends a strand of community."

    menu:
        "Spend the evening writing letters to Marisora residents":
            "You sit under the string lights, pen steady, composing letters that are as much ceremony as communication. Each line holds reassurance and accountability. You seal them with a bit of soil tucked inside—literal soil as a talisman."
        "Go up to the rooftop and plant the first mangrove seedling with Elias":
            "You and Elias pat the soil with reverent hands, mud under your nails. Planting the seedling feels like booking a claim against future storms: a small, stubborn belief that growth is possible."

    # --- merge ---
    "The evenings and early builds fold into months of shared labor and small victories."
    # [Scene: Rooftop Garden at Night | Months Later | Twilight]
    hide maya_reyes
    hide rita_ortega
    hide elias_jun

    scene bg ch14_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Lush strings swelling gently into a warm, steady chord]
    # play sound "sfx_placeholder"  # [Sound: Night insects, far water lapping, the murmur of neighbors below]
    "Time unfolds into labor and small rituals. You measure those months in milestones: the greenhouse frame going up without rain for the first time, the first batch of modular cages holding juvenile prawns that skirted a"
    "fragile silver sheen, the first successful communal meal where everyone contributed from their plots. Arlo Benitez spills his water filters into a pond and then, embarrassed, turns it into a learning session for children. Rita Ortega"
    "curates a community mural that stitches Marisora and the new town together in bright paint."
    "Elias Jun is both near and distant in the rhythms of the work. Where he cannot be, he builds. Where you cannot be, you plan. The relationship stretches like a net—wider, stronger, holding the weight of"
    "shared purpose and occasional frayed strands. You learn to adapt: swapping shifts so one of you can teach a class while the other staffs the greenhouse, passing small parcels—mangrove seedlings wrapped in damp cloth, jars of"
    "preserved fish, letters folded until creased—between trucks and trains."
    "One evening, you stand on the rooftop with Elias Jun, the tide-watch on your wrist catching the lantern light. The tide-watch ticks on, a small instrument of continuity. You plant another seedling together, your fingers cradling the tiny root ball like something fragile and important."
    show elias_jun at left:
        zoom 0.7

    elias_jun "I miss the harbor's creak. I miss the compass of your dad's boat and the bakery's timing. But look at this—' (he gestures at the rooftop, at the rows of seedlings) '—we've made a small coast here."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We've made a coast of ritual and soil. We haven't erased what was lost; we've given it a place to live, a way to be tended."

    elias_jun "Sometimes I worry we'll forget how to be mariners and become gardeners instead."

    maya_reyes "Maybe mariners garden better than gardeners sail. Either way, we're learning."
    "Elias Jun: (kisses the tattoo of the tide-watch on your wrist) 'Promise we keep writing?'"

    maya_reyes "Promise. And visiting."
    "They are simple words, but they are contracts sealed not on paper but on routine: shared errands, quixotic parcels, and a calendar of boat rides folded into downtime."
    "Dr. Ayla Voss comes up to the rooftop that night with a thermal mug. Her nod this time carries less of the unreadable weight and more of a careful approval."
    show dr_ayla_voss at center:
        zoom 0.7

    dr_ayla_voss "You've built something resilient—not only infrastructure but a practice of care. That's rare."

    maya_reyes "We had a lot of help. We had to let go of some things we loved to make room for others."

    dr_ayla_voss "There will be people who disagree. There will be reports and audits and critiques. But you chose a path that preserved life in a pragmatic, human way."
    "The words are not absolution; they are recognition. You accept them as fuel."
    hide elias_jun
    hide maya_reyes
    hide dr_ayla_voss

    scene bg ch14_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Swell into hopeful choir-like harmonies, then settle into a warm piano]
    "Months roll. There are visits back to Marisora—short, heart-heavy pilgrimages where you touch familiar wood and count what remains. You leave behind maps and plans to neighbors who chose to stay. You keep a ledger of"
    "the names you carry with you, and sometimes you read them into the evening like prayer."
    "Leaving was a wound. It is also a kind of fidelity—the difficult, slow maintenance of love across distance."
    show elias_jun at left:
        zoom 0.7

    elias_jun "Do you ever regret it?"

    "After a long silence, the answer is both precise and soft" "I regret some things. But not the choice to move when staying would have been to see people we love swept by what we could have prevented. We traded one form of presence for another—less about geography and more about sustained care."
    "There are hard nights. Budget whispers in the corners. A bad storm tests the first modular barrier you helped design; a shipment of seedlings is delayed; old friends in Marisora call with news that is heavy."
    "Each setback is a test of the repair skills you taught yourselves. You meet them the way you learned to meet storms: with plan, with community, and with hands ready for work."
    hide elias_jun

    scene bg ch14_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Quiet piano, a single ascending line resolving into major harmony]
    "On a clear evening, with the new town's lights turning gold across the estuary, you and Elias Jun plant the largest mangrove sapling so far. Neighbors gather—some cooking, some talking, some simply watching. The sapling's roots"
    "are thick and stubborn. You bury it deep, your palms dark with soil, and for the first time in months a tide of something like calm rises in your chest."
    "We did not stop the sea. We learned its language and made a new kind of shore."

    "Elias Jun (pulls you close)" "This is our home now—patchwork and brave and always in motion. We will keep doing the slow things."
    "You breathe in the salt and river algae and the faint smoke from someone's dinner. The scent does not replace Marisora's harbor; it layers over it. Memories live beneath and alongside these new routines."
    "Rita Ortega: (shouting from below) 'Party on the ground floor in twenty. Bring your pots!'"
    show arlo_benitez at left:
        zoom 0.7

    arlo_benitez "I've saved some of the first harvest for you, Maya!"
    "You laugh, and the sound stitches the rooftop to the town below. The ache of leaving is still there, a thin tide at your ankles, but it is accompanied by the solid, warm weight of daily purpose and shared labor."
    hide arlo_benitez

    scene bg ch14_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Lush, hopeful orchestration resolving into a gentle major chord]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, low communal chatter, the soft rustle of mangrove leaves]
    "You look at Elias Jun, at Rita Ortega, at Dr. Ayla Voss—at the community you helped carry and the new one you helped raise—and you feel a steady, rising sense that this is enough. Not perfect. Not everything the heart mourns. But enough."
    "You lift the tide-watch to your eye, like a small, private ritual. The second hand moves on."

    scene bg ch14_f99e88_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade into a single warm sustained note]
    # play sound "sfx_placeholder"  # [Sound: Night settles; the town breathes]
    "You are leaving, and you are arriving. You are carrying the harbor's geometry in the shapes of your plans and the texture of your hands. You are building a life with Elias Jun that is both a repair and a promise."
    "You walk down from the rooftop into the glow because there is work to do—and because tonight, there is also time to dance with the people who refused to let loss be the last word."

    scene bg ch14_f99e88_10 at full_bg
    # play music "music_placeholder"  # [Music: Warm piano and strings linger, then fade]

    scene bg ch14_f99e88_11 at full_bg
    "THE END"
    # [GAME END]
    return
