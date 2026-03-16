label chapter6:

    # [Scene: Green Prototype Site | Morning — two days after the council vote]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Insistent percussion under high strings]
    # play sound "sfx_placeholder"  # [Sound: Distant generator hum, sporadic radio chatter, gulls cutting through wind]
    "You wake to the taste of iron in your mouth — not blood, not yet. Just the metallic aftertaste of decisions signed and words said where everyone could hear them. The compass at your throat is"
    "cool, an anchor that feels suddenly too small for the weight you've asked it to hold."
    "The pilot's scaffolding looks fragile in the gray light, like a promise built of borrowed time. You were the one who closed the hall and made the town's governance the condition. You remember the small, decisive"
    "motion of your hand as you pressed for community clauses, the way Elias took your breath with that look — steady, hopeful. Now the hope is elastic and stretched."
    show elias_park at left:
        zoom 0.7

    elias_park "They called last night. The fund — they're pulling the transfer rights demand, but they're pulling the money too if we don't relent on scaling."
    "You let whatever you were going to say hang in the salt-scented air. The truth tastes worse when it gets a name."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "So they leave us with no cash and with the optics of, 'community couldn't scale fast enough.'"
    show nima_shah at center:
        zoom 0.7

    nima_shah "They won't admit it that way. Investors hate uncertainty. They've already sent a press release with a vague line about 'reassessing commitments.'"

    elias_park "We knew this could happen. We put the clauses in because it mattered. But—"

    mara_serrano "But the point is: they wanted to own the town before they would fund it. We said no."
    "Nima exhales, the sound sharp enough to carry. She points at the scaffolding, at the half-planted sedge in the modular planters."

    nima_shah "We can stretch what we have. Re-prioritize materials. Call more volunteers. I can rework the deployment schedule so the sensors get in first."
    "Your chest tightens with a mixture of vindication and dread. Vindication because the clauses are the boundary you drew for what Puerto Alba will be. Dread because every boundary costs muscle: money, time, nights without sleep."
    hide elias_park
    hide mara_serrano
    hide nima_shah

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Pulsing low strings; a single high violin note like a held breath]
    "A municipal truck halts at the site, exhaust stinging and authoritative. Iris steps out — her coat is the same hard charcoal, a municipal pin glinting like a bite of light. She crosses the gravel with everyone watching."
    show iris_varela at left:
        zoom 0.7

    iris_varela "When the town's safety is at risk, the council acts. Emergency municipal funds will cover a partial barrier. It won't be everything. It will be fast."
    "Her voice is the authority you once trusted without question. Now it strikes you like the snap of a line being tightened."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "Partial? On what terms, Iris?"

    iris_varela "Emergency protocols. The municipality assumes responsibility for certain sections. We'll prioritize the main promenade and the old wharf. It will hold for the near term."
    "Abuela Rosa stands at the fringe of the group, outline hunched against wind. Her hands are folded into each other like prayer, her eyes a map of tides and losses."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "It will hold for some storms, niña. Not for all. We know this."
    "You move to her, needing the steadiness of roots."

    mara_serrano "They'll try to spin this as us versus them."

    abuela_rosa "They will try. But you stood where it mattered."
    "The municipal trucks unload men with machine drills. Volunteers arrive in clumps — fishermen with calloused hands, teenagers with scarves flapping, Abuela's neighbors with thermoses. The work begins with a rhythm: hammer, plank, shout. The pilot slows to a crawl as labor shifts from funded machines to human muscle."
    hide iris_varela
    hide mara_serrano
    hide abuela_rosa

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tools, strained laughter; a child's voice calling a joke that lands flat]
    "You find Mateo at the front line, a familiar shape bent over a rope. He grins when he sees you, but the edges of his smile are raw; he's been carrying nights of watchfulness."
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "Thought you'd sleep in and let me handle the heavy lifting, huh?"
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "Not today."
    "He elbows you, the motion a claim of friendship and of shared fatigue. You shoulder a sack beside him. The cold bites at your wrists; the smell of wet rope and diesel is the new normal."

    menu:
        "Inspect the sensor wiring before lifting":
            "You kneel beside the wiring, fingers numb as you trace braided cord and shriveled tape. The moisture sensor blinks irregularly; you tap it and make a note on the corner of your palm. It will be one more thing to fix tonight."
        "Take the front line with Mateo now":
            "You hoist the sandbag with Mateo. The weight pushes on your back like truth. For a moment, the two of you move as one — propulsive, stubborn — and the world narrows to rhythm and grit."

    menu:
        "Send volunteers to reinforce the seam now":
            "You shout orders; a dozen pair of hands answer. Sandbags are thrown into place like urgent stitches. People move with that peculiar intensity of those who have to choose between fear and action."
        "Focus on sensor data to predict weakest points":
            "You drag Elias and Nima to the LED banks. Together you triangulate the strain points. The plan is clinical — but in the time it takes to validate, the sea gets closer."
    "THE END"
    # [GAME END]
    return
