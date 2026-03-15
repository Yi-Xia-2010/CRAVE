label chapter1:

    # [Scene: Marisol Marshes | Morning]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping against barnacled pilings, distant gull cries]
    # play music "music_placeholder"  # [Music: Low, mournful strings; a single piano motif underlines the wind]
    "You step off the bus with your chestnut hair damp from the morning fog. The field jacket feels a little tighter across your ribs—there's a weight there you can't sling off, like a wet rope looped"
    "through your shoulders. Salt beads on your eyelashes. The marsh exhales the same scent you remember: brine, old rope, and the faint, stubborn sweetness of decayed marsh grass. It smells like the town's memory."
    "You walk the boardwalk. The wood gives underfoot, small protests muttered in long-forgotten knots. Waves nudge at the warped planks and you watch the water find the same weak places it always has. Each little gouge"
    "seems to map onto a face you can't stop seeing. The ache in your chest is a stone."
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "I suppose it was only a matter of time before something pulled me back."
    "A gull peels off and the sound is too bright against the gray."
    hide amina_reyes

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A vendor's kettle clanging, faint conversations, the smell of fried fish and citrus]
    # play music "music_placeholder"  # [Music: A single mournful accordion thread plays low]
    "At the market, stalls sag from last night's rain. Someone is frying fish over a small propane burner; steam and citrus peel crackle together. You move through the stall-lined corridor and the town unfolds in its"
    "usual, exasperating ways—familiar and fragile. People glance up as you pass; some nod with the careful recognition of people who have measured absence before. You keep your gaze loose because you are not ready for all"
    "the faces you know."
    "Marina spots you first. Her seashell pins catch the light, warm on her braid. She steps forward with a smile that tries to be steady; there is relief in it, and something else—harder, sharper—at the edges."
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "Amina! You made it. I didn't think you'd actually come back for this season."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I couldn't not. Not when the marsh started writing its complaints in high tide marks."

    marina_lopez "You're dramatic. Come on—breakfast at Town Hall. Lucia's making her speeches early; she insists on the eggs."
    "Her hand brushes yours as she steers you toward the municipal building. The contact is brief and old-friend casual and somehow stitches something small in you for a moment."
    # [Scene: Town Hall / Planning Office | Morning]
    hide marina_lopez
    hide amina_reyes

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of a coffee urn, low murmurs of gathered townsfolk]
    # play music "music_placeholder"  # [Music: Quiet, tension-tinged strings]
    "Mayor Lucia Varela stands near a folding table of coffee and scrambled eggs, her brass lapel gleaming like a small sun. She fills the room with the precise gravity of someone who has carried bad weather as a ledger and learned the arithmetic of compromise."
    "Mayor Lucia: [warm, businesslike] 'Amina. You came back earlier than I expected. Sit—don't stand like a ghost at your own homecoming.'"
    "You let her guide you into a folding chair. The fluorescent lights are harsh on the maps. Dr. Kenji Sato sits close by, his fingers tracing lines on a printout as if he can will the waters into a different logic."
    show dr_kenji_sato at left:
        zoom 0.7

    dr_kenji_sato "The models updated overnight. Tidal inflows this season are higher than our summer projections—localized amplification from the new channel formations. We need both short-term shelter plans and longer-term marsh response strategies."
    "You flip open your battered waterproof notebook. The pages crackle; the smell of varnish and salt rises up—tangible, like a promise you've been carrying. Your pencil hovers over a blank margin, an invitation and an indictment both."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I ran the numbers again on the living shorelines prototype. If we combine native reed restoration with targeted eelgrass beds and a phased boardwalk retrofit, we reduce peak inundation at the inlet by measurable amounts—and preserve habitat. It won't be as fast as a wall, but—"
    show mayor_lucia_varela at center:
        zoom 0.7

    mayor_lucia_varela "—and it will take political patience, money we don't have now, and coordination with the regional authority. You know that, Amina. I taught you budgeting once; you remember it well."
    "There is a laugh threaded with metal in her voice. You feel the old teacher-student geometry—what she taught you then is what you must now translate into options they can vote for."

    dr_kenji_sato "The science supports combined approaches. But there are thresholds—if we cross certain storm surge levels repeatedly, infrastructure fails faster than communities can adapt. That's the blunt truth."

    amina_reyes "We adapt the flows, not just the infrastructure. We can't keep throwing up higher walls without paying for what that cost will be to our marsh."
    hide dr_kenji_sato
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "And what about the kids? My students—"

    mayor_lucia_varela "We all understand who we're protecting, Marina. That doesn't make the ledger lighter."
    "The words hang between you, a ledger of human lives and ecological lines. You taste coffee and iron at the back of your throat."

    menu:
        "Offer Kenji your field data to compare notes":
            "You slide the notebook across; Dr. Kenji's eyes brighten at the sketches, and he begins to mutter possibilities about calibrating his models to local microhabitats."
        "Keep your notes private for now":
            "You tuck the notebook closed, tucking yourself inward. Kenji nods, small and unreadable; the moment feels like a missed bridge."

    # --- merge ---
    "Continue"
    hide amina_reyes
    hide mayor_lucia_varela
    hide marina_lopez

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant mechanical hum; the whisper of rain on aluminum]
    # play music "music_placeholder"  # [Music: A slightly brighter, hopeful synth undercurrent that feels out of place]
    "Across the marsh horizon, Elias Hart's field office gleams: a modular blue trailer, laptop screens glowing, a 3D-printed model of the proposed sea-wall under a clear dome. It looks like a pledge—clean lines, neat promises. The sight of it tightens something in you."
    "Elias Hart steps out from the office, tablet at his hip, sleeves rolled with the practiced ease of a man used to convincing rooms. He smiles when he sees you. The smile is a tool he uses well; it is calibrated to reassure."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Amina. Good to see you. The model's been updated too—we can run a localized simulation if you have a minute."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Always a simulation with you, Elias. Do the simulations include what the marsh actually gives up when you shore it off?"

    elias_hart "They include trade-offs. But I'm trying to minimize the harm. We can protect the center, keep businesses, and save lives. That's not nothing."

    amina_reyes "It's something—and it is also everything the marsh cannot be if you seal it. I keep thinking about what we lose when we fix things fast."

    elias_hart "I know the loss is real,' (he says, softer), 'but I also know negligence when I see it. Amina, we can build systems that are strong and integrate living elements. Give me a chance to show you the hybrid designs."

    amina_reyes "Show me then. And show me the parts you can't model—how people will fish, how the birds will find the new channels. Show me that the money doesn't mean erasure."
    "The conversation stretches. There is civility; there is steel. You share more than polite facts now—each sentence carries a measurement of trust."

    elias_hart "I want this to work as much as you do. Maybe we disagree about the order of operations. Maybe we disagree about the speed. But we both want Marisol to still be here."

    amina_reyes "That's not the same as wanting the same thing for the same reasons."
    "Elias Hart gives a small, resigned smile. You both know that's true, and the silence blooms heavy between you."

    menu:
        "Run your fingers over the model's miniature wall, imagining its shadow":
            "Your fingertips catch the cool plastic. For a second, you can almost see how the light would change on the water—and also what would be shaded out of existence."
        "Turn away and scan the marsh instead":
            "You turn your head, watching the reeds. That small motion steadies you; the marsh answers with a hush, like an old friend listening."

    # --- merge ---
    "Continue"
    # [Scene: Niko's Boatyard (Memory) | Late Afternoon in recollection]
    hide elias_hart
    hide amina_reyes

    scene bg ch1_Start_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow rasp of planes on timber in your memory, the distant slap of a repaired sail]
    # play music "music_placeholder"  # [Music: A single acoustic guitar, warm but edged with sadness]
    "You don't go into Niko's boatyard this morning—you don't have the courage to disturb the salted air with your present weight—so instead you let memory ferry you there. The boatyard blooms in your mind: tar smell,"
    "salt-stiff rope, a multi-tool with a familiar engraving. You remember the curve of a keel you once helped sand, the stubborn way Niko taught you to hold a plane."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "You don't sand like that. You're thinking about the shape, not the grain."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I'm thinking about whether it will last the next storm."

    niko_kaur "Then you'll be sanding a long time. Boats like people; they'll tell you when they're done."
    "The memory quickens and blurs—Niko's laugh, a carved wooden locket ticking against a palm, the day the sea took something that never returned. You feel the locket's weight again in your chest."

    amina_reyes "I left when I thought I could learn how to prevent it. I returned and still feel I left."
    "The guilt is an old companion—familiarly heavy, stubbornly present. It has taught you to be careful and to over-explain yourself. It has taught you to bite down before you say things that hurt."
    # [Scene: Rooftop Community Garden / Evacuation Shelter | Midday]
    hide niko_kaur
    hide amina_reyes

    scene bg ch1_Start_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Small feet—the distant laughter of children; water trickling from a hand-held sprinkler]
    # play music "music_placeholder"  # [Music: Low atmospheric pad, threaded with quiet tension]
    "The rooftop garden is a green square against the overcast. String lights pend from poles, and someone has pinned a hand-drawn evacuation map to the notice board. The space is a compromise—part sanctuary, part contingency. Marina"
    "moves between beds, checking soil moisture, and her students' laughter filters up like small hopeful things that don't yet know the ledger."
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "Some of them asked if the sea will touch their beds this year. They have an honest way of asking that hurts."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Tell them the sea is a teacher and a thief sometimes. Tell them we are trying to keep it from both."

    marina_lopez "You always say things like that—poetic and half-impossible. How are you, really?"

    amina_reyes "I'm tired. And I'm afraid the choices we'll make will be the kind that leave people behind, even with the best intentions."
    show dr_kenji_sato at center:
        zoom 0.7

    dr_kenji_sato "We can buy us time with certain adaptations, but the social component is the hard variable. That's politics. That's people choosing who moves, who stays."
    "You stand at the edge of the roof and look toward the field office again. The trailer's lights are steady. The model of the wall glints. The town looks smaller, more fragile, than the maps suggested."
    "The marsh seems to breathe shallowly, as if the season itself were holding its breath."

    amina_reyes "This season will demand choices that cost us all,"

    marina_lopez "Then we'll tally carefully."
    "There is a promise in her voice that tries to be enough. It is not enough to unstone the weight in your chest."

    menu:
        "Stand and watch the field office until someone speaks to you":
            "You fix on the trailer's glow until the light blurs; the waiting is its own argument, a test of patience and resolve."
        "Help Marina with the seedlings to quiet your hands":
            "You kneel by the beds and the soil gives under your fingers. The work steadies your breath; the tenderness is a small, necessary rebellion against the season's hardness."

    # --- merge ---
    "Continue"
    # play music "music_placeholder"  # [Music: Tension strings swell, then taper into a single unresolved chord]
    hide marina_lopez
    hide amina_reyes
    hide dr_kenji_sato

    scene bg ch1_Start_7 at full_bg
    "You close your notebook for a moment and press your palm to the cover. The leather is worn; your fingers find the small friendship bracelet tucked into the spine, its threads frayed. You think of the"
    "brother you lost—of all the ways you tried to learn, to be better, to be there—and you feel the old guilt like a tide."
    "The day moves on; people disperse to meetings and inspections, to gossip and graft, to repair and to policy. The maps will be redrawn, the models will be run, the meetings scheduled. You know the season will not wait for grief to finish its work. It will demand decisions."
    "You watch the field office's LED blink. The 3D model under the dome sits immaculate and dangerous in its promise. The marsh bends and does not break, for now."
    "You breathe in the salt and the damp and let the sound of a gull fade into the low hum of many conversations. A meeting is called for later; a vote will approach in smaller, cautious"
    "steps. Voices around you shift from greeting to strategy, and the room grows dense with possibilities that are also threats."
    "You feel the tide of the season rising in a different register—rumors and promises, political pressure and quiet, stubborn rebuilds. You tighten your hand on the notebook until the leather creases."
    "The choices are coming. They will not be simple. They will be costly. They will, in some ways, hurt people you love."
    "You stand there as the afternoon light goes thinner and the town's architecture seems to lean into itself, preparing."

    scene bg ch1_Start_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
