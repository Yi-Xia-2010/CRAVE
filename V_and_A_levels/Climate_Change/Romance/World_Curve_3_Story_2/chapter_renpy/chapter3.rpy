label chapter3:

    # [Scene: City Hall Annex — Council Chamber | Late Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, sustained cellos — patient, weighty.]
    "You step through the doors with your notebook still damp from Tidewatch's fog tucked against your ribs. The multi-tool in your pocket presses a familiar ridge into your palm; salt and ink cling to your hands."
    "The room's clinical air seems to try to polish the salt off you and everything it touched back home: weathered docks, your brother's laugh, the damp green of a marsh at dawn."
    "At the center table, Elias Voss is already seated. His navy suit is a geometry of clean lines; his fountain pen rests like an accusation on the polished wood. He looks at the room the way a tide reads a shore—measuring, calculating what to take."
    show elias_voss at left:
        zoom 0.7

    elias_voss "Good morning. Thank you all for coming. Elara deserves a solution we can trust—one that protects property and brings investment. My team has modeled a seawall that will hold up to storm surges and unlock the waterfront for redevelopment. The numbers speak."
    # play sound "sfx_placeholder"  # [Sound: A soft click as his rendering advances; the projection fills the wall with smooth concrete and ribboned promenades.]
    "He speaks like a man reciting an inevitability. The renderings are seductive: a straight line across a chaotic edge, lights, tourists, glass. They make risk look tidy."
    "Rosa Tan, hands knotted on her tote, stands before the council with a voice that's already frayed."
    show rosa_tan at right:
        zoom 0.7

    rosa_tan "Those renderings mean bulldozers in our cove and boats shoved into dry slips. I've seen it. We've lived the 'fix' that fixes investors and forgets people. We can't let short-term gains erase who we are."
    "Rosa's words vibrate against the chamber's cool surfaces. Her urgency slices through the polite theater of debate."
    "Ben Harper, leaning on a cane he keeps more for habit than need, clears his throat like gravel."
    show ben_harper at center:
        zoom 0.7

    ben_harper "They brought a 'seawall' in '94. Cost a fortune. Took our slips. They told us protection. What we got was empty storefronts and a waterfront that didn't know how to breathe. My father told me storms were born of mistakes like that."
    "Ben's voice is not loud, but it carries the weight of memory. Each syllable is a ledger: boats, names, lost wages. The room listens because none of them know how to argue against that kind of history."
    "Professor Noor rises and moves with the steady, unflashy rhythm of someone who has spent decades coaxing data into honesty."
    hide elias_voss
    show prof_noor_azizi at left:
        zoom 0.7

    prof_noor_azizi "Our models—Maya, if you will show the sediment core—suggest that living barriers can reduce sediment loss and attenuate wave energy in ways that complement localized defenses. A phased pilot on the Saltmarsh can be monitored for five years. It's not instantaneous protection; it reduces risk while maintaining ecosystem services."
    "You feel the air tighten when Noor says 'not instantaneous.' That word hangs between the polished plans and the people's livelihoods like a seam you are expected to mend."
    hide rosa_tan
    hide ben_harper
    hide prof_noor_azizi

    scene bg ch3_98c6f2_2 at full_bg
    "Elias tilts his head, the faint gleam along his cheekbones catching the LED light."
    show elias_voss at left:
        zoom 0.7

    elias_voss "With respect, Professor, living systems are beautiful in theory, but when a Category Four hits, municipal leaders don't get to say, 'We'll wait for nature.' They need walls they can point to. They need certainty for investors. The timeline is a political reality."
    "He smiles, precise. The smile is a dam."
    "You rise before the question can be practiced into warmth. Your voice is steadier than you expect."
    show maya_soler at right:
        zoom 0.7

    maya_soler "We aren't asking to wait for an apocalypse. We're proposing staged interventions — living breakwaters paired with targeted hardpoints where necessary. That's not romanticism; it's resilience that keeps livelihoods intact and keeps the fishing economy functioning during transition."
    "Elias leans forward, pen tapping like a small metronome."

    elias_voss "Ms. Soler, your passion is admirable. But passion doesn't balance a municipal budget. Investors want a signal. A seawall sends a signal that the town is secure."

    maya_soler "And a seawall signals that the sea must be turned out of sight. It erases the place that raised us. It replaces nets and salted cod with polished storefronts that don't belong to our people."

    "Council Member (off)" "Ms. Soler, we understand the cultural stakes, but the mayor has asked for a plan that guarantees protection."
    "The council's language is a sterile tide; it erases nuance. You can feel the air narrowing, the room becoming a socket that only certain shapes can fit into."
    # play sound "sfx_placeholder"  # [Sound: A brief, sharp cough from the back row. The scrape of a chair.]
    "Aiden Kuro sits in the public gallery near the back, amber eyes narrowed. He doesn't stand. He just looks at you—a complex, unreadable expression that pools hurt and something like accusation. The sight of him burns like salt on a fresh scrape."

    maya_soler "Aiden—"
    "He meets your eye and then looks away, jaw tight. You can't tell whether he thinks you're naive, dangerous, or simply defeated. The uncertainty gnaws."
    "Rosa interrupts, words tumbling, hands animated."
    show rosa_tan at center:
        zoom 0.7

    rosa_tan "If we let Elias bulldoze through, we'll lose not just land but memory. Volunteers—people who grew up here—will stand up to maintain living structures. We will steward them. We will work."
    "Elias's reply sharpens like a knife hidden in a velvet glove."

    elias_voss "Volunteers are noble, but they are not engineering firms. I can deliver construction contracts, maintenance plans funded by developers, immediate jobs. That's what keeps roofs over heads tomorrow, Ms. Tan."
    hide elias_voss
    show rosa_tan at left:
        zoom 0.7

    rosa_tan "At what cost? To what community?"
    hide maya_soler
    show prof_noor_azizi at right:
        zoom 0.7

    prof_noor_azizi "The data show lower, long-term maintenance costs for hybrid approaches. Also—' (she turns toward the projection, pointing) '—we can design seawalls in tandem with nature, but it requires governance and time. The independent review we propose would clarify the performance envelope."
    "Elias's jaw tightens, a manual clamp. He leans in, voice even."
    hide rosa_tan
    show elias_voss at center:
        zoom 0.7

    elias_voss "An independent review is a delay tactic. Delay costs money. Time, in politics, equals lost support. There's a window for investment, Ms. Soler. Miss it, and the funds go elsewhere."
    "You feel the room tilt. 'Window' is a currency you aren't sure you can buy."

    menu:
        "Ask Noor to show sediment-core results now":
            "You gesture to Noor; she brings up a close-up of the sediment cores. The depth of peat and invasive fill is visible—a slow-history that speaks of time, not speed."
        "Call out Elias's developer partners by name":
            "Your mouth opens; you clamp it. The names hang like tinder. You decide not to toss a match yet. The room holds its breath."

    # --- merge ---
    "The meeting proceeds as the presentation shifts."
    "Elias shifts, and the projection slides into an animation of finished promenades. The sound of waves on shore is replaced by the hum of economic opportunity—cafés, boutiques, and a promise that everything will look polished and safe."
    "Ben stands again, voice thin as a tide's receding whisper."
    hide rosa_tan
    show ben_harper at left:
        zoom 0.7

    ben_harper "We've been promised protection before. We were promised modernization. But the sea remembers. Hats and suits can't tell you where the rip currents are. My granddaughter's education doesn't mean she should lose her home to a plan that forgot people."
    "Council murmurs, papers rustle. The balance of the room feels like a scale that's been slowly tipped by a gust."
    "You feel your chest tighten—a deep, familiar contraction. Guilt rushes in: brother, the flood that took him, the nights you stayed awake trying to stitch a safer tomorrow from shoals and seedlings. You have carried responsibility like a wet coat, and it clings now."

    menu:
        "Step closer and speak of your brother's flood":
            "You tell the room about the night the water came too fast—how your brother misread the tide and how that failure haunts your work. Faces soften. Aiden Kuro's mouth twists; he clears it but doesn't speak."
        "Keep your appeal strictly technical":
            "You fold emotion into graphs and projections. The council nods at numbers. Elias Voss smiles a little; the human cost blurs into columns. Your chest empties a fraction; the room responds in the language it prefers."

    # --- merge ---
    "The chamber returns its focus to procedural questions."
    "Noor's hand finds yours for a second as you step down from the dais. It's a small grounding touch—scientific and human at once."

    prof_noor_azizi "However this goes, document everything. We're on a knife-edge between immediate protection and long-term resilience."
    "Elias's voice, when he speaks again, is low enough that the microphones strain to catch it."

    elias_voss "This vote isn't just local—it's a statement to investors across the region. You can vote for a living pilot and be brave, but you may forgo critical funds now. Or you can move forward with a seawall that guarantees protection and development. It's your call."
    "The phrase 'it's your call' lands like a gavel-shaped stone."
    "You look out across the chamber: Rosa's hands clenched, Ben's lined face, Noor's steady posture, the council members shuffling their notes, Elias composed and wickedly sure. The fate of nets, docks, and small kitchens seems to rest on the hinge of a single meeting."
    "Your throat is dry. The salt on your fingers feels like a map of obligations. The room contracts and waits. Voices quiet to a low susurration, like wind pressing on a window."
    "A councilmember clears her throat, the procedural rustle of democracy about to click into motion."

    "Councilmember Diaz" "Ms. Soler, the chamber requires a public stance from the proponents. As a lead on the living-infrastructure proposal, how do you recommend we proceed? A pilot program? Full continuation of the engineering plan? A combined approach with conditions?"
    "Your mouth forms the words you have been rehearsing and arguing for in your head for months. Each syllable is a stone you could choose to set into the foundation of your town—or a rock that might topple other people's lives."
    "You can feel the arousal of the room ascend—measured, not frantic—each heartbeat a small drum."
    hide prof_noor_azizi
    show maya_soler at right:
        zoom 0.7

    maya_soler "—"
    # play music "music_placeholder"  # [Music: A single, taut violin string rises.]
    # [Scene Pause: The chamber leans in. The choice will split futures.]

    menu:
        "I publicly endorse the living‑breakwaters plan and ask for a pilot.":
            jump chapter4
        "I open negotiations with Elias, seeking concessions to protect fishermen.":
            jump chapter8
        "I threaten to expose Elias's conflicts and demand a delay pending independent review.":
            jump chapter12
    return
