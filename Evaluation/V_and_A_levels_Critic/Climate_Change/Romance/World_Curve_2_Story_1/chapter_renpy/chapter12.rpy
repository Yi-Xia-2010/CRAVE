label chapter12:

    # [Scene: Municipal Hall — Council Chamber | Late Afternoon, Cold Rain]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain tapping hard against tall windows; an intermittent muffled horn from the harbor]
    # play music "music_placeholder"  # [Music: Tense, driving strings — pace quickens]
    "Narration"
    "You step back into the chamber as if into a machine whose gears are made of language and obligation. The projector's cold rectangle paints faces in pale blue; breath fogs on the glass. Your palms still"
    "smell faintly of camera leather and salt. The flyer folded in your pocket feels like a small, fragile thing against the hard lines of policy about to be drawn."
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We need both speed and safeguard. Is there legal language that can reconcile them? Mister Sato, the town can't wait through another season."
    "Narration"
    "You are the conduit everyone keeps glancing at—the person who knows the marsh maps, who has a camera full of before-and-after frames, who can translate angry, granular pleas into something the council will sign."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "We do not trade our toe-hold for promises that evaporate. Those covenants have to be ironclad—public access, the marsh beds, the nursery plot behind my house. If it's not in the clause, it's not protected."
    "Narration"
    "Etta's voice is smaller than she is, but it cuts across the room. You feel the weight of her history in each sentence—decades of seed trays, of naming every stretch of eelgrass—pressed into a demand for words. The room leans with her."
    show elio_sato at center:
        zoom 0.7

    elio_sato "Binding covenants slow construction. The firms we're contracted with can't operate under indefinite easements; they need certainty. We have engineers' timelines, supply chains—time is not experimental. We can begin within weeks with the baseline contract."
    "Narration"
    "Elio's words fall like scaffolding: efficient, heavy, impossible to ignore. You notice the micro-gesture you have watched in him before—the tightening at the corner of his jaw when he says 'we'. It's the only sign of feeling you get from someone who otherwise insists on metrics."

    councilor_rosa_menendez "We need both speed and safeguard. Is there legal language that can reconcile them? Mister Sato, the town can't wait through another season."
    "Narration"
    "You open your mouth and close it. There is a tide in your chest—rising, and with it the knowledge that any phrase you endorse could be the hinge for years. You think of Etta's greenhouse, of"
    "Jun's boat, of the kids who race along the pier. You think of Mateo's look this morning—there, then not—complex and unreadable—and the way his hands had hovered over his notebook before he folded it shut."
    hide councilor_rosa_menendez
    show jun_park at left:
        zoom 0.7

    jun_park "Speed means mouths filled and roofs mended. It also means boards go up and people get priced out. We can't pretend displaced folks won't be counted as collateral."
    "Narration"
    "Jun's hands drum the table. The words vibrate through your boots. The murmurs in the chamber spike and retreat like small storm surges against a bulkhead."
    hide etta_hargrove
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "Structural defenses are necessary, Ari. We can't paper over the math. But if you let the barrier be the only answer, you lose the living systems that actually absorb—"

    elio_sato "Mr. Alvarez, this is not the time for hypotheticals."

    mateo_alvarez "This is exactly the time. We keep them in the conversation or we lose the work entirely."
    "Narration"
    "Mateo's fingers sift a tide chart in his hands; despite the calm in his tone, his face is lined with an unease he won't hand over to anyone. He does not leave. He does not step"
    "fully inside the shove. His stance feels like distance—measured and public—a thin partition you can only see through. It makes the room colder."
    hide elio_sato
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "Tell them how the marsh works. Tell them that walls are only as good as the ground under them. And tell them the town built with one another, not for a profit margin."
    "Dialogue — Multi-Turn (Etta & Elio Sato)"

    etta_hargrove "If your contract displaces families and privatizes access, what then? The nursery? The kids' crab lines? Who signs for that loss?"
    hide jun_park
    show elio_sato at left:
        zoom 0.7

    elio_sato "Loss is relative, Ms. Hargrove. There are metrics—economic recovery, infrastructure stability, decreased emergency costs. We are preventing catastrophes."

    etta_hargrove "Are you preventing the people who live next to those catastrophes? Or are you cataloguing them as acceptable damage?"

    elio_sato "My aim is to minimize harm across the region. Fast, engineered solutions save lives."

    etta_hargrove "Do they save the life that was built by hands like mine, or do they save only the structures on a ledger?"
    "Narration"
    "Words ricochet. The room smells of wet wool and coffee that has been reheated too many times. Your watch ticks with the nervous insistence of a metronome. Outside, rain thumps like a deadline."

    menu:
        "Read Etta's covenant wording aloud":
            "You clear your throat and read the covenant phrases—'public easement', 'non-transferable community stewardship'—each term landing like a pebble in a pond. Several faces visibly relax while others tighten. Etta nods, small and fierce."
        "Summarize the covenant into pragmatic bullet points":
            "You paraphrase: protect key parcels, enforce access, include review periods. The room murmurs approval—the language is leaner, more digestible, but Etta's fingers clench under the table. She gives you a look that says: careful."

    # --- merge ---
    "The discussion continues in the chamber."
    "Narration"
    "The choice you make releases different sounds in the room. Reading Etta's full language presses the stakes into the air; summarizing is a pressure valve that feels like compromise. Either way, you are shepherding something living"
    "into the machine of policy, and you feel the strain of that translation in your throat."
    # [Scene: Saltmarsh Flats | Early Evening — Low Cloud, Slanting Rain]
    hide mateo_alvarez
    hide etta_hargrove
    hide elio_sato

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind in reed tips, the soft creak of sills settling into mud]
    # play music "music_placeholder"  # [Music: Percussive, heart-pounding rhythm]
    "Narration"
    "You go out with Etta and Jun to the flats to show the council what exactly might be at stake. The marsh smells of iron and brine; the ground sucks at your boots. The restoration plots look fragile—coir lines braided like tiny barricades against the water."
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "These are living defenses. They take time. If the barrier goes up first and the mud is boxed off or dredged, they die. We've already seen failed trials where the ground was starved."
    show jun_park at right:
        zoom 0.7

    jun_park "We can't stop people from needing roofs. But we can keep a place to come home to. The covenants buy that time."
    "Narration"
    "You kneel beside them, fingertips in cold peat. The mud clings like a promise and a threat. You think of the timeline Elio keeps repeating—'weeks'—as if human lives align neatly to construction schedules. You feel the urgency like a tightening rope in your chest. A storm season looms with teeth."
    "Narration"
    "A drone of boots approaches—council staff returning from other meetings, carrying legal pads. The town moves around you, small and necessary, and the pressure accrues."

    menu:
        "Take photos of the restoration plots for the committee report":
            "You lift your camera, the shutter clicks; close-ups of roots and coir, flags in the mud. Later, these images will hold the room accountable—they're evidence. Etta smiles, gratitude softening her face."
        "Record a short voice note from Jun to play at the council":
            "You speak into your phone: Jun's hands describe the cost of losing a boat, the taste of failed nets. The rawness of his voice later makes Councilor Rosa look up in a way the charts never do."

    # --- merge ---
    "You proceed back toward the town with material to present."
    "Narration"
    "These small acts are quiet resistance. They don't stop contracts, but they make the cost of losing people legible. Still, each photograph, each voice note, is only a bandage against something larger, and the clock's teeth edge nearer."
    # [Scene: Etta's Greenhouse (The Nursery) | Night — Amber Light, Heavy Air]
    hide etta_hargrove
    hide jun_park

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant thunder; the greenhouse's small ecosystem sighing]
    # play music "music_placeholder"  # [Music: Low, urgent cello — heartbeat tempo]
    "Narration"
    "You retreat with Etta and Mateo to the greenhouse to refine the committee language. Inside, the air is warm and peppery; it feels like a pocket of unreality compared to the wind-bent streets outside. Seed trays glisten. The nursery is a small mercy."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "I understand the need for covenants. I also understand that without swift protection, some of those people won't survive the next surge. I'm asking—no, I'm warning—don't make 'binding' synonymous with 'immobilizing'."
    "Narration"
    "He looks at you—not accusing, but cautious. You can feel the distance between you like a draft. His hands, callused from handling prototypes and tide instruments, hover over the seedlings. You want to tell him everything"
    "you've seen, every worry; instead, you try to make language hold both urgency and care."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "Binding doesn't mean immobility. It means legal teeth against extraction. It means my greenhouse stays open to everyone, not a lawn behind a wall."

    mateo_alvarez "Then give me the language and I will push for modular designs that can be integrated. But if the contract locks the town into a narrow path—"
    show elio_sato at center:
        zoom 0.7

    elio_sato "Ms. Hargrove, Mr. Alvarez, Mrs. Tanaka—time is the variable here. Every week you spend adding clauses is a week of exposure for citizens."
    "Narration"
    "The speaker crackles. Elio Sato's interruption is a reminder that some voices carry institutional weight even when they are remote. You are in the middle: Etta with her seedlings, Mateo with his prototypes, you with the translator's task. Each sentence you shape could close a door or wedge one open."
    "Dialogue — Multi-Turn (Ari Tanaka & Mateo Alvarez)"
    hide mateo_alvarez
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "If we insist on covenants, they will slow construction. Elio says ‘weeks’; Jun says 'we lose people'. We are wedged between two necessary truths."
    hide etta_hargrove
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "Then we have to hybridize. Enforcement mechanisms and fast builds. Pilot sections. Adaptive clauses—review periods. We can't sign something that destroys the marsh in the name of speed."

    ari_tanaka "Can you push that in front of the council? You said you would stay in the conversation."

    mateo_alvarez "I will if the conversation includes real audits. I won't be the engineer who builds a wall that forgets its neighbors."
    "Narration"
    "You want to reach for his hand, to anchor him and yourself. You don't. The greenhouse smells of wet soil and decisions unmade. Time thins."
    "Narration"
    "Your internal pulse matches the thunder. The stakes are sharp: covenants that could keep the town's soul intact, contracts that could buy immediate safety at social cost, or a public fight that could expose hidden data"
    "but risk a storm arriving before defenses are ready. You have been asked to shepherd opposition voices into the committee's language; that task has become a pivot on which dozens of lives tilt."
    # [Scene: Municipal Hall — Council Chamber | Night — Storm Approaching]
    hide elio_sato
    hide ari_tanaka
    hide mateo_alvarez

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, building roar outside — wind gaining; the microphone hisses]
    # play music "music_placeholder"  # [Music: Strings at a crescendo; percussion pounding — very high intensity]
    "Narration"
    "You return to the chamber with concrete language drafts, images, voice notes, and the greenhouse's damp optimism clinging to your coat. The atmosphere is tight with exhaustion and the knowledge of deadlines. Councilor Rosa looks at you with an expression that asks for both moral courage and practical deliverables."
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We must vote on the committee recommendation tonight, Ms. Tanaka. The firm requires an answer. The state has deadlines. There is a safety window before the forecasted nor'easter."
    show elio_sato at right:
        zoom 0.7

    elio_sato "A timely agreement will allow us to mobilize crews before the storm. Delay compounds risk."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "So will signing away the marsh. If you let them build first and ask questions later, you'll have paid for permanence with our people's homes."
    hide councilor_rosa_menendez
    show jun_park at left:
        zoom 0.7

    jun_park "We can't let fear of the storm become the excuse to erase us."
    hide elio_sato
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "I can't endorse a plan that doesn't include audits and modular integration. If you accept the baseline without those things, I won't be part of that process."
    "Narration"
    "Mateo's refusal lands like a wave hitting a boat—sudden and urgent. It's not an attack; it's a boundary. His withdrawal from full endorsement is a pressure that makes everything tilt."
    "Ari Tanaka"
    "The room tightens around you. Every piece of evidence you gathered is suddenly both weapon and plea. The legal counsel murmurs about liability clauses. Elio Sato's team projects cost models and timelines like armor. Your chest hurts. The storm outside presses its weight against the windows, a physical drumroll."
    "Dialogue — Multi-Turn (Ari Tanaka, Councilor Rosa, Elio Sato, Etta)"
    hide etta_hargrove
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "We can demand binding covenants that protect community lands and public access but include staged mobilization windows, audit requirements, and a dispute resolution clause."
    hide jun_park
    show elio_sato at left:
        zoom 0.7

    elio_sato "Such additions introduce ambiguity and would require renegotiation with contractors. We risk losing the current bid and the window to deploy before the storm."
    hide mateo_alvarez
    show councilor_rosa_menendez at right:
        zoom 0.7

    councilor_rosa_menendez "If we lose the bid, do we accept the risk of delay? If we accept the bid, do we accept the risk of displacement?"
    hide ari_tanaka
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "This is not abstract. It's our nursery behind a clause, it's Jun's boat listed as collateral, it's kids who won't have a place to fish after school."

    elio_sato "And if we delay and a surge hits—how many lives are we counting as acceptable?"

    etta_hargrove "How many lives will be counted as acceptable if the town becomes privatized in the name of safety?"
    "Narration"
    "The argument spirals, overlapping like the weather outside. Your head buzzes. You can feel the very room humming with stakes and people. It is almost unbearably loud in your ribs."
    "Ari Tanaka"
    "You have been asked to shepherd the opposition's language. This is the moment where your stewardship turns into decision. You can push for covenants with teeth, accept the baseline for speed, or call for a public"
    "audit and campaign that could slow the process and reveal hidden factors. Each choice has its own brand of moral fracture."
    "Narration"
    "Your pulse is a drum. Rain hammers the roof. Files shuffle like a shifting shoreline. The council waits, the firm watches, the town holds its breath. This is the point the machine stops whirring and asks you, naked, which gear to engage."

    menu:
        "Negotiate strict covenants protecting community lands and public access.":
            jump chapter14
        "Accept the company's baseline contract to ensure swift construction.":
            jump chapter18
        "Launch a public campaign demanding audits and transparency, delaying the contract.":
            jump chapter21
    return
