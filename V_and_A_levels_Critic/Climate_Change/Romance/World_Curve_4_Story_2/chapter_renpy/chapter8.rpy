label chapter8:

    # [Scene: Ferryworks Greenhouse | Night]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet drip of water from an overhead pipe; the muted click of Jun's laptop keys]
    # play music "music_placeholder"  # [Music: A tight, urgent string ostinato underlaid with a steady electronic pulse]
    "You push open the ferry's hatch and the greenhouse breathes its own heat against the night: wet soil, solder fumes, the sweet, briny tang of leaf and tide. Jun is hunched over a scatter of printouts"
    "at the workbench, the lamplight turning his recorder into a tiny, red planet. The memo sits between you like a trapped gull — white paper, blacked-out headers, and a paragraph that folds policy into leverage."
    "You take it with hands that remember how cardboard soaked through the last flood. The first sentence is a cold, precise thing: thresholds, triggers, automatic relocation clauses calibrated to financial tolerances. The language is engineered to look like safety; the effect is displacement dressed as algorithmic inevitability."
    "Your notebook opens like a constable's ledger. You write, brutally and quickly, a single expletive that lands on the page with the same weight as a hammer blow. Then another, then a line of strategy—who to call, who to show, what to leak first."
    show jun_park at left:
        zoom 0.7

    jun_park "They embedded it in the trigger matrix so it looks like a risk-management tool. But the thresholds align with land-value curves—it's designed to make low-income zones statistically disposable."
    show ava_maren at right:
        zoom 0.7

    ava_maren "They wrote the calculus to pick winners and losers. They hid the lever where only numbers can find it."
    "Jun rubs his temples. His voice is precise and bright with rage, the kind of outrage that sharpens rather than clouds. He slides a folder toward you: annotated timelines, email headers, a list of internal project codes that map to Saltway's sectors."

    jun_park "If this goes public raw—we force transparency. But investors panic when certainty fractures. Panic triggers clauses of its own: funding freezes, emergency takeovers. We need pressure without giving them financial whiplash that boots people out before the ink dries."
    "You taste the arithmetic like iron. The worst outcomes are not storms but paperwork and profit margins that build walls where homes were."
    hide jun_park
    hide ava_maren

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant truck reversing in the yard; the greenhouse's heater clicks]
    "Maya's footsteps are quick on the gangway. She arrives with a stack of printed leaflets and a string of battery lanterns; her face is lit from below, fierce and immediate."
    show maya_lin at left:
        zoom 0.7

    maya_lin "We can stage the press showing tomorrow at dawn. Jun, you time-stamp the docs. Ava, you'll speak. We'll bring witnesses. The lawyer—if you want to run a legal play, we'll give them every tape."
    "You fold the memo to protect it in your jacket, the paper warm against your ribs like an argument that must be kept alive."
    show ava_maren at right:
        zoom 0.7

    ava_maren "We need to control the narrative. If they call us hysterical, they win. If we make the memo the center but frame it with people's stories—tenure, the bakery that rebuilt three times, Old Mara's tale—then it's harder to gaslight."
    show jun_park at center:
        zoom 0.7

    jun_park "I can have a report prepped for a coordinated release—hard copies to select outlets, an embargo if you want to pace it. Or we go full on: streaming this, live testimony. Control the frames, control the sympathy."
    "The greenhouse hums like a held breath. You can feel the neighborhood leaning into you, a rope of expectation taut in your chest."

    menu:
        "Blurt the worst of it out now":
            "You open your mouth and let the anger that tastes like salt spill—'They've algorithmically decided who stays.' Jun's eyes sharpen and he nods, faster plans trading in the air."
        "Breathe, make the plan measured":
            "You breathe down to the bone, scratch 'coordinated release' in your notebook, and outline a timeline. Jun's shoulders relax fractionally; the method steadies the immediate surge."

    menu:
        "Ask him to stay close—don't roam":
            "You tell him, almost pleading: 'Stay after—if it rises, don't go chase it alone.' He pauses, small and honest: 'I'll anchor.' He means it."
        "Let him do it his way—trust the craft":
            "You say, 'Do your thing. Make it beautiful.' He laughs, relief leaking into his voice, and you picture his hands soldering under a streetlamp, distant and necessary."

    menu:
        "Raise the memo and demand immediate hearings":
            "You feel the weight of the paper as a weapon; your voice cuts across the pier—'Hearings now. Public, recorded, enforceable tenure.' Cameras lurch toward you. A murmur of affirmation rises from the crowd."
        "Request a coordinated embargoed release with Jun":
            "You lower the memo, proposing a measured, legal release—'We time this. We lock the evidence.' Jun nods, grateful for the discipline; the crowd waits, less seized but steadier."
        "Signal Ori to unveil the art-stunt first":
            "You nod to Ori. He lights the panels; an audible intake from the crowd ripples through the pier as seaglass and circuits bloom into light. Emotion floods feeds; you see faces soften, but legal counsel's expression is unreadable."

    menu:
        "Stage a mass public exposure—march with evidence and demand immediate hearings.":
            jump chapter9
        "Work with Jun for a legal exposé and coordinated media release to force policy change.":
            jump chapter15
        "Create a humanizing art-stunt with Ori—reshape the narrative visually, then release evidence.":
            jump chapter13
    return
