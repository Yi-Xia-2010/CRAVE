label chapter1:

    # [Scene: Tidewatch Harbor | Late Afternoon]
    # play music "music_placeholder"  # [Music: Low, salt-wind ambient with distant gull calls]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boardwalk planks creak underfoot; a camera shutter clicks in the near distance]
    "You step off the regional shuttle and the harbor takes you like a smell: brine, old diesel, and something small and green — kelp dragged in and drying like lace. Your olive field jacket still smells"
    "faintly of bus seats and coffee, the brass compass locket warm against your throat under the scarf you never stopped wrapping around your neck. The Moleskine thuds against your hip when you shift; the elastic is"
    "frayed in the same place your mother used to smooth with a thumb."
    "The boardwalk is as battered and beautiful as memory. Salt has eaten the railing into a scalloped edge; someone nailed a string of torn festival banners back together with twine. Rain from last night sits in"
    "shallow pools where the boards dip — neon magenta from the Old Pier's broken sign pools into one, as if the town's past is bleeding color back into the present."
    "You inhale, and the brine is immediate."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "Maya. You actually came back."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You still call me that. Do I ever stop earning it?"
    "Samir sets the camera down and gives you a long look, as if he's scanning for changes in your shadow. He steps closer; the wooden bench between you smells of old rain."

    samir_reyes "You look like you slept in that jacket for three days straight. Is that the same locket?"
    "You feel the brass under the scarf, its coolness a small, private compass. You let the corner of your mouth lift."

    maya_reyes "Same locket. Don't make it sound like an heirloom auction."
    "Samir laughs, the sound coming out as something softer than mockery. He gestures at the pier, then at the cluster of fishermen repairing nets."

    samir_reyes "Town looks the same. Different. You should've seen the market a year ago—Maren had all those pamphlets out. You left for research, came back and the whole town's got pamphlet-box syndrome."

    maya_reyes "Pamphlet-box syndrome?"

    samir_reyes "You know—everyone thinks a flyer will do the work of a hand. Anyway.' He taps the camera, then you, bringing the tone down like lowering a flag. 'Why now, Maya? Last I heard you were knee-deep in models up north."
    "You sense the question is both practical and gentle curiosity. The harbor's wind pins a stray hair to your cheek. The thing you did years ago — the policy that eased immediate suffering then and left"
    "neighborhoods exposed later — sits at the back of your throat, salt and unsaid. You could explain. You could stay vague. Your hands instinctively find the Moleskine."

    maya_reyes "I came home to listen. And to see if what I learned can help here. That's always been the plan."

    samir_reyes "Listen, huh.' He studies you, like he's trying on that word for size. 'Well, listen then. Also—(he nods toward the docks) Elias Hart is out there, barefoot as always. He's been muttering about a community meeting tonight."
    "You turn. On the far dock, silhouetted against a puddle-mirror of the sky, Elias Hart is exactly how memory paints him: sandy hair messy from the salt wind, sleeves rolled up, barefoot toes gripping the wood."
    "He spots you and lifts a hand — a small, quick wave that feels illicit and whole."

    menu:
        "Smile and wave back":
            "You lift your hand without thinking. The gesture is light; Elias's grin brightens in the dull light, and for a second the harbor feels like a room you're invited back into."
        "Keep your head down and walk toward Samir":
            "You let your shoulders close in as if you could tuck yourself small between the boards. Samir reads the move and smirks, then points you toward the Glasshouse like he's sending you on purpose."

    # --- merge ---
    "The scene continues."
    # [Scene: The Old Pier | Late Afternoon]
    hide samir_reyes
    hide maya_reyes

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant hammering, the rhythmic slap of a rope against a mast]
    "Elias Hart calls out as you approach, voice carrying over the salt-slick air."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Maya! Back for good or just to glare at the skyline?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Back for a while. Depends how many meetings I tolerate."
    "Elias Hart walks toward you, shoes in his hand. He still collects small things in his pockets — a scrap of rope, a candy wrapper with a marine biology fact scrawled on it. When he stops"
    "in front of you, he leans against the railing, close enough for the scent of the sea to mix with his laundry soap. There's relief in his face that makes your chest do something awkward."

    elias_hart "Samir said you were coming. The co-op's been trying to keep things afloat while the council talks contracts. There's a lot of talk, not enough hands."

    maya_reyes "How's the fish run looking?"

    elias_hart "Thin. It's been thinning. But people are shifting—trying new nets, different schedules. We're figuring things out in the ways we can.' He tilts his head. 'You have that look, Maya. The planning look. The kind that makes people hand you maps."

    maya_reyes "If I make maps, I want them to be useful to the people who actually live on the lines."
    "Elias Hart's smile softens. He reaches into his satchel and pulls out a folded flyer, edges salt-stiff."

    elias_hart "That's why we need you. Listen—(he breathes in as if the rhythm of his words will steady him)—there's a meeting at the co-op tonight about a redevelopment pitch. Maren Voss's team and a few outside investors, you know the type. People are scared. Some think it's the only way to get jobs back."
    "You nod. The words 'jobs' and 'protection' are always the same trading currency in Harborwell: votes, survival, promises. The tug you feel is not just professional now; it's threaded with memory and the weight of the"
    "promise you made to your mother — to keep Harborwell whole. It presses, gentle but insistent."

    elias_hart "You should come to the meeting. Even if it's just to listen. Having you there would...help."

    maya_reyes "I'll be there. I need to visit the Glasshouse first. Julian wanted to show me some updated projections."
    "Elias Hart's expression changes, a quiet note of something like hope."

    elias_hart "Good. I want to hear what you think. About everything."
    "The conversation folds into a lull where the only sounds are the tide and a gull's distant cry. It is ordinary and, because of that, heavy with possibility."
    # [Scene: Glasshouse Research Lab | Early Evening]
    hide elias_hart
    hide maya_reyes

    scene bg ch1_Start_3 at full_bg
    # play music "music_placeholder"  # [Music: Subtle, scientific hum; footsteps on tile]
    # play sound "sfx_placeholder"  # [Sound: Julian's soft, deliberate tapping on a touchpad]
    "Professor Julian Kim meets you in the foyer. He looks exactly like a person who lives in perpetually half-saved notes: spectacles slightly askew, cardigan with a faint coffee stain, thermos in hand."
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "Maya. You returned at a good time. Or a timely one, if you prefer data-speak."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Timely is about as hopeful as statistics get."
    "He offers you a smile that is more affectionate than professional."

    professor_julian_kim "You always preferred numbers with names attached. Come—I've set up the models we ran last month."
    hide professor_julian_kim
    hide maya_reyes

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft whoosh as the hologram rotates; quiet beeps of model runs completing]
    "Professor Julian Kim gestures at the layered map with a practised hand."
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "Sea-level rise trajectories are unchanged in their trend. Seasonal intensification has accelerated in the last five years. But look here—this overlay shows what small, targeted interventions could do if we act within a five-to-ten-year window."
    "You lean in, fingertips brushing the cool glass of the projection case. The models are familiar — they move with the logic that made you leave in the first place — but seeing them in the place where your training and this town meet makes something inside you settle."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "The projections match regional trends. But the social overlays…do they account for displacement pressure if a large-scale redevelopment goes through?"
    "Professor Julian Kim's eyes soften. He taps the socio-economic layer until neighborhoods light and dim like bioluminescent plankton."

    professor_julian_kim "That is the core question. Models can show hazard reduction, but they can't tell us who bears the burden. That's where planners like you come in — you read the numbers and decide what 'fair' looks like."

    maya_reyes "Fair is expensive."

    professor_julian_kim "True. But inaction is more costly, and sometimes less visible. You know that."
    "You do. The policy you signed once — meant to provide quick relief — is a ledger of invisible costs that have sat with you like grit. Julian's tone is not accusing; it's factual, a steadying presence."

    professor_julian_kim "We need someone who can bridge the lab and the docks. Someone who can explain trade-offs without making them sound like inevitabilities. Frankly, Maya, I hoped you'd be that person."
    "You swallow. The harbor's wind seems to follow you even here, whispering at the glass."

    maya_reyes "I'll help. But I need to speak to the community first. To listen to the fishermen, the shopkeepers, the people whose names are on these overlays."

    professor_julian_kim "Good. Start with Samir and Elias Hart. They've been keeping pulse. And come by the lab anytime — the door's open."
    "There is warmth in his invitation that you aren't sure you deserve, but you accept it the way you accept the locket around your neck: because it is handed to you, and because it matters."
    # [Scene: Abandoned Sea Wall / High-Tide Field | Evening]
    # play music "music_placeholder"  # [Music: Low tide hum, a string instrument bowed slowly]
    hide professor_julian_kim
    hide maya_reyes

    scene bg ch1_Start_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves lapping at concrete, distant town bells marking the hour]
    "You find the Abandoned Sea Wall like an old scar — jagged, awkward, undeniably part of the landscape. The concrete is cold under your palm; sea spray pins salt to your lashes. In the tide pools,"
    "clouds float fractured and still. Each pool is a small mirror with its own sky."
    "You climb onto the wall and sit, boots beside you, hands braced on the pitted surface. The town behind you feels small and stubborn; the sea before you is patient and indifferent. You reach for the compass locket out of habit."

    menu:
        "Open the locket and touch the photo inside":
            "The tiny photograph is folded thin, your mother's fingers pressed into it from where she smoothed the edges. For a second you let the memory rule — her laugh, the way she planted beans in the cramped garden. It steadies you, makes the promise feel less like weight and more like direction."
        "Keep the locket closed and take notes instead":
            "You slide the locket back under your scarf, tucking your hands into your journal instead. You write the horizon's outline in small, precise lines — elevations, tide marks, a note about the pattern of gulls — and the act of cataloguing quiets the ache into something useful."

    # --- merge ---
    "The scene continues."
    "The past compromise — the policy you authored that patched urgent holes but left long seams — sits in your chest like grit. It does not scream. It is a low, ongoing presence. You think of"
    "the families in the lower neighborhoods, the shopfronts that woke to floodwater a year longer than they should have. You think of your mother pressing a weathered hand to your cheek and asking you to keep"
    "the place where she grew old safe."
    "You close your eyes and map the promise in your head: not a single solution, but a web of small, deliberate acts stitched with community consent. The thought is not triumphant; it is an arrangement you can make with yourself. It feels possible."
    "Behind you, the town's murmurs soften into evening — someone calling their dog, the distant radio playing a local station. The sky is a slate promise. In your journal you draw a line from the Glasshouse to the docks to the neighborhoods cradled behind the boardwalk, a clean, patient stroke."
    "You breathe in the cold air, the sea-sour tang filling your lungs, and the harbor seems to watch you back, patient as tide."
    "A small flicker of something — possibility, perhaps — stirs like a moth near a lamp. It is quiet, almost embarrassed to be hope. You let it be."

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: A gentle upward strain, still muted]

    "You write a single line at the top of a blank page" "Map what matters."
    "It feels right, and unfinished."
    # [Page-Turn Moment: You close the journal, feeling the weight of a plan forming that will require both data and hands. The harbor's evening light gathers around you like a soft insistence — not a demand, but a direction.]

    scene bg ch1_Start_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
