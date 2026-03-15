label chapter2:

    # [Scene: Nueva Mar Municipal Hall | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant rumble of the tide like a sleeping machine; footsteps echo on polished floor]
    # play music "music_placeholder"  # [Music: Low, sustained cello undercurrent]
    "You step into the municipal hall still carrying the heat of the Low Row on your skin, the salt clinging to the cuffs of your jacket. The place is cool in a way that feels intentional"
    "— air conditioning, cleaned edges, a kind of institutional detachment that smooths the city’s rougher sounds into manageable data points."
    "Your maps and prints sit like a small, damp weight under your arm. You breathe and feel that same tightening from before: not panic, but a slow, corrosive worry that eats at the edges of confidence."
    "You imagine the marsh in diagram lines, the community garden roofs, Lio’s paint-splattered hoodie on a future that might be half-erased."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft mechanical whirr; the muted chatter of municipal staff]
    # play music "music_placeholder"  # [Music: Single cello note repeats, hollow]
    show mayor_ana_velez at left:
        zoom 0.7

    mayor_ana_velez "Good morning. Thank you for coming early. We want this to be efficient."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Efficient at what cost?"

    mayor_ana_velez "At protecting the city. At moving funds that keep people dry. We are trying to balance immediacy and feasibility."
    "You study her scarf, the way she tucks it against her neck, as if warmth and optics can be the same thing. The atrium smells faintly of coffee and lemon polish. It feels like standing under a glass dome when outside the city is being rewritten in saltwater."

    menu:
        "Step closer and speak plainly":
            "Maya Corvin closes the distance, steadier than she feels. 'Feasibility for whom, Mayor? The wall's timeline makes zero room for the community design we’ve built.' Her words land and the Mayor’s smile tightens for a fraction longer."
        "Keep your distance and listen":
            "Maya Corvin stays where she is, arms folded over her prints, letting the Mayor and her aides outline the agenda. Listening keeps her in control; she measures the gaps she’ll have to fill later."

    # --- merge ---
    "Continue with Elias Kahn arriving."
    show elias_kahn at center:
        zoom 0.7

    elias_kahn "Maya."
    "He gives you a look that says he knows your stakes."

    elias_kahn "I read your summaries. I know what you and Rafi have been doing."

    maya_corvin "Then you know we need more than the narrow window they’re offering."
    "Elias shifts, glances at a staffer, then lowers his voice."

    elias_kahn "The timeline is—tight. Investors have staged funding tranches, and indemnities as written favor quick, large-scale vendors. The legal team says a turnkey seawall is the most defensible route."

    maya_corvin "Defensible for them. What about the livelihoods we’re trying to keep? The wetland corridors? The nursery roofs?"

    elias_kahn "I sympathize. I do. But consensus matters in these votes. If we push too hard publicly without a plan that looks 'municipal-ready,' Mayor Velez will go with the path that produces the fewest legal headaches."
    "You watch his hands — the weathered notebook — and feel the old, familiar friction: his carefulness against your impatience. It feels like two different languages translating the same grief."

    maya_corvin "Consensus feels like compromise when people with power set the terms. How do I convince you—convince them—that what we have is real engineering and not just sentimental patchwork?"

    elias_kahn "You already have technical rigor. Dr. Sima agrees with your models. The issue is political optics, Maya. A community plan needs a deliverable format, a staged budget, and guarantees that legal counsel can accept. I can help translate it. But I can’t promise votes."
    "You want to ask whether promises are enough. You want to press until something gives. Instead you press a hand to your map, feeling the paper between your fingers like battlements."
    hide mayor_ana_velez
    hide maya_corvin
    hide elias_kahn

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The controlled click of polished boots; a faint whir of a drone casing tucked in a case]
    # play music "music_placeholder"  # [Music: The cello draws a minor chord, thinly]
    "Camila 'Kai' Navarro is exactly as expected: immaculate jacket, blade-sharp bob, steel-gray eyes that appraise you as though you were an object set before a problem to solve. Her suit’s modular seams catch the light like armor."

    "Camila 'Kai' Navarro" "Ms. Corvin. Elias."
    "We appreciate the municipality making space for a rapid response. Time is a resource getting chewed by the sea."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "Time is a resource—so is the memory of the place you intend to cut through."

    "Camila 'Kai' Navarro" "Memory doesn’t stop waves. Our model protects critical infrastructure and most residences. The design is scalable and tested. Delays increase risk."

    maya_corvin "Scalable for whom? Your footprints clean the map of messy neighborhoods and living systems until nothing recognizable is left."

    "Camila 'Kai' Navarro" "We save people. Policies are cruel in theory; engineering is precise. If emotion costs lives, then the choice is clear."
    "Elias watches this exchange with the look of someone trying to keep ice on both sides of a churning sea."
    show elias_kahn at right:
        zoom 0.7

    elias_kahn "Kai, there are valid points in both approaches. Could we—"
    "(he searches for language that will hold)"

    elias_kahn "—pilot a hybrid? Allow the community model to be documented in a format compatible with the municipal contracting process?"

    "Camila 'Kai' Navarro" "Pilots add months. Investors require certainty. A hybrid means more moving parts, more liabilities. We offer a proven barrier now. That is the package on the table."
    "The conversation coils and uncoils. Everyone speaks in the currency of contingencies: funding tranches, indemnities, investor confidence, legal defensibility. You feel each word like a tide mark rising slowly and erasing the lower edges of the Low Row from the map of what the city will be."

    menu:
        "Push Elias to commit publicly to the hybrid idea":
            "Maya Corvin looks at Elias squarely. 'Say it here, Elias. Tell them the municipality will at least open the tender to include hybrid bids.' He hesitates; the notebook between his hands trembles imperceptibly. 'I—I'll ask for that language in the memo,' he replies, softer than she wanted but still something."
        "Call out Kai directly on the human cost":
            "Maya Corvin leans in toward Camila 'Kai' Navarro. 'How many livelihoods does your model condemn to relocation because it’s faster for investors?' Her steel gaze meets yours. For a second you see something like recognition and then she answers, 'We calculate loss and lives saved. Sentiment doesn’t alter raw mortality in a storm.' The answer lands like flint."

    # --- merge ---
    "Conversation continues with Mayor Ana Velez interposing."
    show mayor_ana_velez at center:
        zoom 0.7

    mayor_ana_velez "We will hold a series of briefings. The corporation will present the technical plan and the municipality will field comments. I urge calm; we must not impede a process that protects the city."
    "You feel the word 'calm' fall over you like a lid. It is an instruction to quiet the small, urgent noises the Low Row makes in your chest — the pump that sputtered last night, Rafi’s voice telling you the weakened seawall is failing in a longer rain."
    "Your pocket buzzes. Rafi’s name lights your screen."
    hide maya_corvin
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "Maya, the pump’s leaking again. Low Row is wet underfoot. If we don’t get something in place, the nursery beds will drown, and Mrs. Ortega’s lower kitchen flooded last night. There’s talk of volunteers leaving if we can’t promise anything."
    hide elias_kahn
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Hold the volunteers steady. I’m here. I’ll press for time at the briefing. We can’t let them sign construction orders without seeing our plan."

    rafi_odeh "Do whatever you can. People are scared, Maya. They need a reason to stay."
    "You tuck the phone away and feel the familiar churn: duty braided with dread. The municipal hall feels suddenly distant, the atrium’s gloss a thin veneer over decisions that will slap into tarps and seedlings and children’s bedrooms."
    "Elias catches your eye across the cluster of officials and gives you a look that says he is on your side in sympathy if not in method."
    hide mayor_ana_velez
    show elias_kahn at center:
        zoom 0.7

    elias_kahn "If you can package it — the community plan — in a sequence that addresses liabilities and deliverables, I’ll carry it to the committee. I can push for a slot on the hearing."

    maya_corvin "A slot isn't a guarantee. They can schedule us at two in the morning and call it participation."

    elias_kahn "Then we make the room and the line of speakers long enough they can’t ignore us."
    "You want to believe him. The hope is a thin filament against the weight of the corporate case made so clinically by Camila 'Kai' Navarro: proof, models, certainty. There’s a gulf you can taste — between"
    "your patched linen and their modular suits; between the soil under your nails and the polished floor of power."
    "Camila 'Kai' Navarro approaches again, this time with a single paper packet in hand — the kind of document that is meant to be indelible."

    "Camila 'Kai' Navarro" "Ms. Corvin, you have passion. I admire that. I do. But the city needs a plan that works under stress. If we delay, more people will be at risk."

    maya_corvin "You make the calculus about risk in spreadsheets. I make it by knowing whose roofs are at the next high tide."

    "Camila 'Kai' Navarro" "Then show me the data you think changes that calculus."
    "Her request is a gauntlet and an opening. You think of Dr. Sima's models, of the rooftop nursery’s retention projections, of the legal forms you need to make them municipal-ready. The tools you have can be"
    "sharpened, but all of it demands time — and the hearing timeline is closing like a door."
    # play music "music_placeholder"  # [Music: The cello recedes into a single held note — tension, thin]
    # play sound "sfx_placeholder"  # [Sound: Quiet hum of the hall; the tide’s distant whisper]
    "You leave the hall with your prints rolled more tightly than before. Outside, the air feels heavier, the city’s salt-warm breath mixing with the municipal coolness you’ve just shed. On the promenade, the Low Row waits like an exposed limb."
    "Your mind rehearses the steps you must take: translate the community plan into budget stages, prepare technical appendices, marshal voices to fill a hearing room, and coax municipal law into tolerating hybridity. Each step seems plausible and perilous in turn."
    "You think of Lio’s nod, Rafi’s urgent voice, Mrs. Ortega’s stew-scented kitchen, the kid with paint on his cheek who still believes in murals. You think of Elias’s cautious promise to try, of Camila 'Kai' Navarro’s clinical certainty, and Mayor Velez’s practiced calm."
    "The anger is slow and steady — not a flare but a deep, weathered burn. The hope is a sliver; small but not extinguished. The worst truth sits beneath both: the city’s machinery is efficient at"
    "erasing complication. It is very good at making decisions that look clean on paper and mean ruin for people whose lives cannot be folded into spreadsheets."
    "You make a choice in the little, private place where resolve hardens into action."

    maya_corvin "We will demand time. We will make them see that community plans are not sentimental — they are survival strategies. We will fill the room. If they set the clock, we will set the agenda."
    "It is not a triumphant decision. It feels heavy and necessary — a small, stubborn defiance edged with the knowledge that saying 'no' to the machine will cost energy, sleep, and perhaps relationships. The thought of"
    "mobilizing your neighbors feels like lighting a line of candles in a hall full of floodlights."
    hide rafi_odeh
    hide maya_corvin
    hide elias_kahn

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: A single, lingering cello note — unresolved]
    "You head back toward the Low Row, the city’s smell changing as you descend — diesel and seaweed and the exact, stubborn scent of life kept going despite everything. The day is not brighter. It is only truer."
    "You are going to mobilize the neighborhood to demand time in the hearing. You do not yet know whether the machine will listen."

    scene bg ch2_c4ca42_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant, patient sound of the tide — relentless]
    # [Page-Turn Moment]
    "You picture the hearing room — chairs, a dais, microphoned voices — and imagine the Low Row’s faces filling it: Rafi with his clay-stained gloves, Lio with his paint-splattered hoodie, Mrs. Ortega clutching a worn photograph."
    "Your chest tightens at the thought of them being reduced to a line-item, of wet gardens becoming collateral damage in someone else’s schedule. The resolve that forms is quiet and very sharp; it will have to"
    "be enough."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
