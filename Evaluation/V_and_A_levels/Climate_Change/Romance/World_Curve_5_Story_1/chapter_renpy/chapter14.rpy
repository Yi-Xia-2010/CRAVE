label chapter14:

    # [Scene: Negotiation Room | Late Evening]

    scene bg ch8_63a6e2_1 at full_bg
    # play music "music_placeholder"  # [Music: Pulsing, urgent synth understring]
    # play sound "sfx_placeholder"  # [Sound: Rain against the windows, a distant gull cut off by the wind]
    "You are still sitting at the long table because you never learned how to leave before a fight is finished. The notebook is closed but heavy in your lap; the leather rubs against your thigh with"
    "the familiar salt grit. The room tastes of coffee gone cold and the metallic tang that comes with deadlines. The projector's light washes everything into clinical cyan—faces, maps, the thin type of the contract clauses."
    "Tamsin crouches by the tablet, eyes skimming legalese with a planner's exasperation."
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Flex language is standard for pilots. It lets us adapt in the field—"
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Adaptation, yes. But not at the cost of oversight. 'Flex' cannot mean 'we decide after we build.' Community governance, binding funding windows, enforceable sunset clauses—these must be actionable, measurable."
    "Corinne's reply is a static blade. She leans back, fingers steepled, the AR halo throwing thin lines across her face."
    show corinne_voss at center:
        zoom 0.7

    corinne_voss "Binding every micrometer of language up front is how projects die. We need operational adaptability. If you tie us down with over-specific clauses, you lose the opportunity—the season, the funding, the maritime window."

    amaya_reyes "And if 'operational adaptability' becomes permanent control? If 'pilot' becomes precedent? You and I both know precedents harden into policy."

    corinne_voss "We can include review points. Independent oversight. We'll fund a community monitor. We want this to work."
    "The room tightens around the word 'monitor'—a cushion of euphemism that could either hold or hollow out protections."
    # play sound "sfx_placeholder"  # [Sound: A chair scrapes. Jules' phone buzzes on the table; he glances at it, face folding in a way that is almost gleeful and almost frightened at once.]
    hide tamsin_cho
    show jules_park at left:
        zoom 0.7

    jules_park "Um. Heads up—there's chatter. Someone's posted our redacted term sheet to a local reporter's feed. It's incomplete, but it shows the pilot's scope and some of the clauses. The reporter's already asking for comment."
    "You blink. For a second the world narrows to the pixel of a notification: a link, a partial document. The taste of metal in your mouth deepens like anticipation."

    menu:
        "Tell Jules to pull it back":
            "You press your palm flat against the table. If it can be retracted, do it. If not—hold everything. (Jules' thumb hovers; his grin is brief.)"
        "Let it breathe — see public reaction":
            "You let a slow breath out. If the leak lands hard, it could force stronger guarantees. But it could also blow trust. (Jules' eyes flick to you, seeking permission.)"

    # --- merge ---
    "Jules' fingers tremble as he taps the screen, then shuts his device. He does not delete the post; he pins the possibility like a small, dangerous flower on the table."
    "Luka Maren stays quiet until the hum of the projector makes space for his voice."
    hide amaya_reyes
    show luka_maren at right:
        zoom 0.7

    luka_maren "I need to say something, too.' (He runs a thumb under his lower lip, trying to make it a joke. It doesn't land.) 'I—I've been offered a research grant. It's substantial. But the letter says collaboration with Voss technicians is a condition."
    hide corinne_voss
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "Was this before or after we started negotiations?"

    luka_maren "After. They approached me two weeks ago. I didn't tell you because I didn't want to make this about me.' (He meets your eyes then, amber frankness against the cyan light.) 'I didn't ask. I wanted to make sure it wasn't leverage."
    "The words land like a stone. You feel the echo—how money can compress choices into one-place solutions, how offers can leave invisible cords around people's decisions."

    amaya_reyes "You should have told me.' (It's not an accusation so much as the recognition of the weight you both carry.) 'We need people who can withstand the pressure when it comes."

    luka_maren "I know.' (He exhales a breath that smells faintly of solder and kelp.) 'I didn't say yes. I don't know yet. But I want to help Marisol, Amaya. I thought I could keep both—"

    amaya_reyes "Keeping both is a luxury some don't get. If you take that grant and Voss's control comes with it, will you still be able to push for community terms?"

    luka_maren "I won't sell out.' (A pause, small and wobbly.) 'But the reality is—resources could mean real protections this season. I can't pretend that's not a temptation."
    "Corinne Voss watches the exchange with a face that reads like an accountant's ledger. She leans forward."
    hide jules_park
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "Luka, I will say this plainly: our technicians can elevate your designs and help scale them. It's not a takeover; it's partnership. No one wants to displace people. Our models show—"

    amaya_reyes "Your models also have assumptions about buy-in and regulatory concessions. Those assumptions are where we need legal guarantees."
    hide luka_maren
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "Amaya, council is nervy. They want the funding. Corinne's team has already been talking to some members. If we push too hard, we fracture the room—"
    "Your chest hits a new cadence: rapid, sharp, like a drumroll. The leak is out. The grant offer sits like an unlit fuse. The council—always the wild card—leans toward immediate funding. The night's timeline has become a narrowing tunnel."
    # [Scene: Voss Marine Solutions Headquarters | Midnight]
    hide amaya_reyes
    hide corinne_voss
    hide tamsin_cho

    scene bg ch8_63a6e2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low mechanical hum, the distant whoosh of climate-controlled vents]
    # play music "music_placeholder"  # [Music: High-paced strings, building]
    "You follow Corinne to the glass wall that overlooks the quay. Inside the HQ the air smells like engineered citrus and something sterile that doesn't exist outside. Corinne taps her holo-pen; a different version of the pilot blinks up—language softened, contingency clauses rephrased into aspirational verbs."
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "We adjusted the language to be workable. Sunset clauses are there. We put in a shared governance board in principle. Democracy takes time, Amaya. You can have safeguards without locking everything into a bureaucratic morass."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "The phrasing matters.' (You step closer to the glass, fingertips cool against the pane.) 'A 'shared governance board' is nothing without binding authority. 'In principle' is not enforceable."

    corinne_voss "And 'binding authority' can be used to stall a project or weaponize objections. We are trying to build a solution before another season hits."
    "A soft chime—Jules again. He is somewhere in the courtyard near the boardwalk, or maybe he is across the hall; the leak folded open into the world and the world is answering. Tweets arrive, a local"
    "reporter's live comments filter through the room, a neighbor's post flares with fear and anger."

    amaya_reyes "The town is already fracturing over perception. Some people read 'investment' as lifeline. Others read 'development' as eviction. If we don't anchor the language in legal teeth, this pilot will be the thin end of a wedge."
    "Tamsin: (quiet) 'I have officers calling me. The mayor wants reassurance. If we force a public legal battle now, we could get national attention. That changes the dynamics—but it also risks Corinne walking away.' (She looks at you like someone asking how much you are willing to gamble.)"

    menu:
        "Confront Corinne now—demand explicit, enforceable clauses":
            "You place both palms on the glass and force the point. Corinne's jaw tightens; the room's humming seems to answer your stroke. (Corinne's smile thins; you can see the pivot of the negotiation.)"
        "Buy time—negotiate cosmetic wins tonight to keep the pilot alive":
            "You soften. You speak of compromise, of shared language that can be audited later. Corinne nods, but you feel the future contracting by an inch. (Tamsin exhales, relieved.)"

    # --- merge ---
    "Your hand is still pressed to the pane. The night outside is thick and moving. Council members you trust—some—are calling Tamsin; their voices are small and tremulous through the static. Corinne's team is polished, practiced at"
    "persuasion. Jules' leak is a public splinter: it draws attention and forces narratives that will be hard to unmake."
    "Luka Maren reaches for your sleeve. The gesture is small and human: steadying, pleading."
    show luka_maren at center:
        zoom 0.7

    luka_maren "If you push the leak and we go public with legal pressure, it could fix this for good. National attention could make Voss come clean—or it could make them leave us with nothing."

    amaya_reyes "And if we accept the watered pilot? We get resources this season. We get to build marshes and test tech. We risk giving Voss institutional footholds that might never leave."
    hide corinne_voss
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "And if you walk away and demand a regulated review, you might stall the pilot entirely. You could force oversight, but Voss could bypass local cooperation and pursue construction through other channels."
    "The room compresses into a single point—the decision you can feel arriving like a swell on the horizon."
    "You can taste the sea and steel together. The rain has stopped; the air smells sharp and alive. The projector's light slices the table; your reflection is deeply doubled in the glass. The arousal inside you"
    "is at its peak—every nerve coiled, every thought a splintered possibility. This is the place where strategy and love and the town's future knot together."
    # play sound "sfx_placeholder"  # [Sound: The projector clicks to standby; the room holds its breath.]
    "You breathe in. You breathe out. The choice blooms in the dark."

    menu:
        "Push the leak and public legal pressure to force stronger legal guarantees.":
            jump chapter17
        "Accept a watered pilot with sunset clauses and community oversight promises.":
            jump chapter24
        "Walk away and demand a regulated review process, stalling the pilot.":
            jump chapter33
    return
