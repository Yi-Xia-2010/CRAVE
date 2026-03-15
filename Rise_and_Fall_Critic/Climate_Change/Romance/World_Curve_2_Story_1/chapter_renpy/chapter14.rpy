label chapter14:

    # [Scene: The Strand | Dawn]

    scene bg ch14_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Slow, hollow cello; distant bell tolling once]
    # play sound "sfx_placeholder"  # [Sound: A truck idling far off, gulls arguing over a scrap]
    "You stand with your palm flat against the damp spine of your journal, the leather swollen from rain and the pressed seaweed pages stubbornly curling. The compass pendant rests cold against your throat. Somewhere down the"
    "Strand, a line of relocation trucks growls—metal making its own kind of tide. You can taste iron and diesel, and under that the persistent ozone of an ocean that keeps arriving in increments."
    "You made the decision. You signed the schedules. You watched men in high-visibility vests map out where fences would go, where foundations would be broken, where the bulldozers would take what the sea might take later."
    "You told yourself you were choosing for the many, for stability, for the city-core cafés and the clinic with its battered satellite dish. You told yourself the ledger demanded it. The sound of the trucks is"
    "a tally."

    scene bg ch14_3be532_2 at full_bg
    "They brought you praise in public statements. Jun's people released tidy photos of concrete poured and lights returned to the waterfront boulevard. Lian's office called you 'decisive' in a release that smelled faintly of printer ink"
    "and citrus. There are lines of congratulations half-wrapped around the city seal. They called it 'necessary.'"
    "You remember each door you closed with a city form in your hand. You remember Rosa's face when she read the clause and then, later, when she pressed her palm to yours as if to stop"
    "something from moving through you. You remember Ivy, furious and small, throwing wet paint at a contractor's boot and getting dragged, for a moment, by the force of a plan you helped authorize."
    # play sound "sfx_placeholder"  # [Sound: Distant shouts, a child's cry muffled by rain]
    "It was never supposed to feel like this."
    # [Scene: Relocation Trucks / Temporary Shelters | Midday]

    scene bg ch14_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Low ambient synth; a steady heartbeat percussion underneath]
    # play sound "sfx_placeholder"  # [Sound: Paper rustling, the soft thud of boxes stacked]

    "You walk among the shelters like someone moving through a series of portraits of what you've chosen. Faces tilt up at you with the slow calculus of neighbors who knew you once as Mara Kestrel before you became "the liaison." Some mouths close when they see you. Others open and the words rotate through" "Why?' 'We were promised—' 'We trusted you."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You thought you could hold the whole town in your hands, hija. You thought you could press a ledger into a people's skin and make the numbers soft. We don't keep ledgers like that."
    "You search for a defense—something practical, something clean—and find only the thin paper of contingency plans and contracts. They flutter uselessly in your mind."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "They said—Jun said—the core would hold. If the harbor businesses survive, we keep the hospital, the pumps, the lines. We can prevent worse loss."

    rosa_alvarez "And what of the worse you have borne down on others? A saved hospital is no comfort if your neighbor loses their home. Numbers are tidy. People are not."
    "You swallow. The tea is already cooling in the thermos. You breathe in the damp wool of your scarf and the smell of cut grass from potted plants someone tried to save."
    # play sound "sfx_placeholder"  # [Sound: Distant shouts, a child's cry muffled by rain]
    "It was never supposed to feel like this."

    menu:
        "Offer to help tend the temporary garden beside the tents":
            "You crouch and cup a mud-streaked sprout between your fingers, distract yourself with the small miracle of green in the gray. Ivy watches you for a long moment; her jaw softens, then tightens."
        "Stand up to speak to the crowd, justify the decision":
            "You climb onto a crate and your voice trembles as you speak the lines you've rehearsed. Some nod. Some look away. A man with salt in his beard asks when his street will be returned. You have no answer that settles him."

    # --- merge ---
    "..."
    # [Scene: City Core | Afternoon]
    hide rosa_alvarez
    hide mara_kestrel

    scene bg ch14_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Taut strings under a cold piano]
    # play sound "sfx_placeholder"  # [Sound: Applause from a televised ribbon-cutting; the clack of heels on wet stone]
    show jun_park at left:
        zoom 0.7

    jun_park "We stabilized the core, Mara. People are safe where it matters. The city will hold, and that gives us time to plan long-term relocation properly."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Safe where it matters for whom, Jun? We left an entire seam of neighborhoods—my neighborhood—open to being taken. We didn't 'give them time' so much as give them a timetable to be moved."

    jun_park "Not every decision is humane, Mara. Some are necessary. You know that."
    "Your fingers find the frayed cord of your compass at your throat and twist it until you can buckle your jaw. You want to ask him for the ledger of how he chose which blocks to"
    "save. You want to know whether he thought of the old boatyards when he signed the map. Instead, you say:"

    mara_kestrel "We promised oversight. The clause—Jun, the clause moves people faster than the money does. Contracts mean nothing if the support isn't there."

    jun_park "We will allocate funding. We'll ensure temporary services—"

    "You interrupt, not intentionally, but the words come hot and sharp: Mara Kestrel" "Temporary services have names. They have elders and children. You sent crews to knock down porches this morning. You called it a 'clearing procedure.' Jun—"

    jun_park "I made the choice to protect the most lives. I asked you to stand with that. You did. We have saved the heart."
    # play sound "sfx_placeholder"  # [Sound: Camera shutters; a distant rumble that might be a bulldozer]
    "His certainty is a blade polished by votes and briefings; it cuts cleanly across the tangled thicket of community. He calls it saving; you carry the names of those who lost their places like splinters beneath your skin."

    menu:
        "Confront Jun publicly, name the neighborhoods lost":
            "You open your mouth to speak to the press—words of accountability—but his team floods the plaza with officials and screens showing 'stability metrics.' Your voice is small in the architecture of spectacle."
        "Walk away with Elias to the Basin, to the mangroves that remain":
            "You find Elias waiting near a patched railing, his sleeves rolled, sensor wristband dimmed. He lets you lead, and for a moment there is no need for words."

    # --- merge ---
    "..."
    # [Scene: The Basin (Late Afternoon)]
    hide jun_park
    hide mara_kestrel

    scene bg ch14_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes, descending]
    # play sound "sfx_placeholder"  # [Sound: Soft rushing of collected stormwater, a muffled conversation nearby]
    "Elias Navin stands where the mud meets a protective reed line, hands tucked into his parka pockets like a man holding together a structure that might fail. He looks smaller than the lab coat photos suggested, but his eyes are steady. He doesn't greet with slogans; he waits."
    show elias_navin at left:
        zoom 0.7

    elias_navin "You did what you thought you had to, Mara. I can't make it look anything other than that."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "You left once. You came back with solutions that needed funding and time. I needed someone to stand with me against the machines when they came. Instead, I helped hand them the keys."

    elias_navin "I remember your father on a night that smelled like old rope and lantern smoke. He called a storm a kind of test—never a sentence. You carry him in how you act. You did not act to make yourself cruel."

    mara_kestrel "It doesn't stop the images, Elias. They sleep under tarps. A woman knitted a hat for a toddler and the hat got soaked when contractors moved a fence into the path to his home. They had to step over their life to get to the food tent."

    elias_navin "I tried to reroute some of the supply chain. I argued for phased support. They overruled me in the meeting that followed the ribbon-cutting. I—' He stops, fingers closing on nothing. 'I can help rebuild what we can. I can help you catalog the harms, demand compensation."
    "You stare at him. There's a way his voice holds facts as if they were talismans, as if the right numbers could call back dignity. But when you look at him, what you don't see is certainty that his plans will be enough to sink anchors into grief."

    elias_navin "I didn't want to be the one saying 'I told you so' when the tide came. I wanted to be with you. I thought if the city could be stabilized, we could build from there. I'm sorry."

    mara_kestrel "Your sorry won't dry out the tents. It won't return the gatherings at the old quay. It will not bring back my father's boatplates."

    elias_navin "No. But I can stay. If you'll let me—help catalog, hold public hearings that actually listen, run remediation trials in the new berms. I want to be useful, not just in apologies."
    "You look at him. He is offering the one thing you couldn't muster: steady, quiet labor, a catalog of small repair acts. Your throat tightens at the thought of accepting his help and letting yourself be cradled in someone else's plan again."

    menu:
        "Take his hand, accept the work ahead together":
            "You reach out. His fingers close around yours, practical and warm. You both kneel at the edge of the Basin and write names into the margins of your journal."
        "Tell him you need time alone":
            "You shake your head and step back into the mud. Elias watches you go, the set of his shoulders like someone preparing scaffolding that might never be used."

    # --- merge ---
    "..."
    # [Scene: The Strand | Dusk]
    hide elias_navin
    hide mara_kestrel

    scene bg ch14_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Single, drawn violin bow; notes stretching thin]
    # play sound "sfx_placeholder"  # [Sound: The steady, distant mechanical breathing of pumps; an occasional distant hammer]
    "You walk the same path you walked a thousand times and find it altered by straight lines of concrete and the silent geometry of decisions. Contractors are finishing the berm. They nod as you pass—professional, polite,"
    "uninterested in the names that fell beneath their wheels. A city councilor on a platform gives another speech praising 'resilience.'"
    "Ivy meets you before you reach the lighthouse where your childhood boat once leaned against good hands and bad knots. Paint still clings to her palms."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "You signed the forms, Mara. You said yes."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I made the call to minimize deaths, I—"

    ivy_kestrel "Minimize deaths? You minimized our lives into statistics and budget lines. My friends are scattered. Mrs. Halverson moved into a shelter three blocks from the clinic that you saved and her medication got delayed. She forgot how to use her inhaler because she doesn't sleep anymore. How is that minimized?"
    "You stand there and feel the ledger in your chest—an account of people you've tried to protect by sacrificing others. It does not reconcile. It weighs heavier by the day."
    "Rosa Alvarez arrives silently behind Ivy and lays her hand on both your shoulders. It is a small, forceful holding that steadies you like an anchor. She doesn't offer platitudes."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "There will be time to build from this. There will be ceremonies, and perhaps, later, a city that learns the wrongs you carry. Whether you survive them depends on how you carry the pain—whether you let it make you cruel or whether it makes you clearer."

    mara_kestrel "I don't feel clearer. I feel—hollowed, as if someone scooped out the part of me that knew how to ask for help."

    rosa_alvarez "Then ask. Even now."
    "You look at the line of newly poured concrete, at the place where the old docks end in jagged teeth. Night begins to settle like a shawl over the city. The marina lights blink on in"
    "the core, warm and assured. The shelters hush under tarpaulin roofs. Public praise circulates like bright confetti and lands on no one in particular."
    hide ivy_kestrel
    hide mara_kestrel
    hide rosa_alvarez

    scene bg ch14_3be532_7 at full_bg
    "They will hang your photo next to the ribbon, and the paper will tell a version of the story that includes your signature and omits the hands that held candles as their porches were taken down."
    "You will be thanked at donor dinners where the food tastes faintly of policy success. You will watch Jun accept a plaque. People will say you 'saved the city' with a tone that implies gratitude and"
    "closure."
    "You will stand, though, at the water's edge and remember the sound of a child's boat scraping a wooden dock, and you will know the cost behind the platitudes."
    # play sound "sfx_placeholder"  # [Sound: A lone bell rings from the Old Beacon Lighthouse, muffled by wind]
    # play music "music_placeholder"  # [Music: The cello returns, lower now; a single, long descending note]
    "You press your palm into the damp paper of your journal one last time and feel the fibers give. You do not cry. The ache is a muscle you've learned to carry and to hide. A"
    "reporter catches your eye and asks for a quote about 'resilience.' You say something measured, something that fits in a headline."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "We did what we could to protect the most vulnerable infrastructure. We didn't do it perfectly."
    "Elias Navin watches from the Basin, hands folded, as if watching weather fronts. Ivy stands beside you, patched and fierce. Rosa's hand squeezes yours once and then releases."
    hide mara_kestrel

    scene bg ch14_3be532_8 at full_bg
    "Public praise tastes of a different salt than the ocean. It crusts over the open wounds. You are praised and hollow. You are leader and ledger and, beneath it all, a person who cannot unmake what has already been moved."
    # play music "music_placeholder"  # [Music: The strings fade; the wind takes the rest]

    scene bg ch14_3be532_9 at full_bg

    scene bg ch14_3be532_10 at full_bg
    "THE END"
    # [GAME END]
    return
