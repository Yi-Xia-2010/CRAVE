label chapter9:

    # [Scene: Town Hall — Conference Room | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Quickening strings under a steady pulse — urgent but hopeful]
    "You smell boiled coffee and varnish. The air carries the faint grit of salt blown in from the open window; it tastes like the edge of every decision you've made for this town."
    "You came because Celeste asked you to meet alone. You came because you wanted to move—fast, if necessary—but not at the cost of everything you've sewn into the Commons. You came because she promised to put"
    "relocation funds on the table, and that promise alone could keep half your neighbors from losing the roofs over their heads."
    "You fold your hands on your satchel. The copper bracelet at your wrist is warm from your skin; the engraved coordinates feel like an anchor against your pulse."

    scene bg ch7_453e40_2 at full_bg
    show celeste_park at left:
        zoom 0.7

    celeste_park "Mara. Thank you for coming on such short notice."
    "(she hands you a glossy executive folder)"

    celeste_park "I know time is a premium for you. I won't waste it."
    "Her voice is even, conversational—precise, the way someone who writes briefs speaks when they want you to listen. There's a smile, measured to be disarming."
    "You register the layout of the table: a map of the promenade's footprint, highlighted in warm colors; a printed draft of 'community benefits' with bullet points; legalese that snakes across a page. The relocation fund line sits in bold, an offer that hums like an engine in the room."
    hide celeste_park

    scene bg ch7_453e40_3 at full_bg
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "I asked to sit in to ensure the science is represented, Mara. But I also wanted to listen."
    "(she inclines her head)"

    dr_amina_bhatt "There are things here that could be engineered safely—if we keep the checks."
    "She meets your eyes and there's no theatricality: only a steady, professional concern. Amina's presence steadies the air."
    "You breathe. You want to start with the Commons—where seedlings, salt pans and memory occupy the same beds as grit and resolve—but Celeste's first words put the carriage of her offer forward."
    show celeste_park at right:
        zoom 0.7

    celeste_park "We propose a full-scale promenade: a raised commercial spine, integrated floodwalls, and a continuous civic front. Funding—secured. Relocation assistance—committed. In exchange, we'd like an agreement limiting disruptive protests on the construction corridor and flexibility for certain engineering methods that ensure the project's viability."
    "You feel the words land like a tide against rock. It's the language of trade-offs: infrastructure for compliance, money for maneuvering room."
    "You let the silence stretch. It ripples across the table like a small current."

    menu:
        "Accept the coffee she offers":
            "You take the ceramic cup. The warmth steadies your palms; for a moment the world narrows to steam and the quiet between heartbeats."
        "Set the cup down untouched":
            "You set the cup down with a subtle clack. It's a small show of weight—an unvoiced boundary before negotiation. Celeste notices, the tilt of her head almost imperceptible."

    menu:
        "Press for the binding pilot clause now, in the room":
            "You press your palm flat on the table and name the clause you want—monitoring authority, public access to data, escrowed release of funds tied to milestones. Celeste listens, and for the first time you see the edges of a concession forming in her face."
        "Ask for time to talk to Elias and Amina before deciding":
            "You ask the question out loud: time. Celeste's smile doesn't vanish, but her fingers tap a quick rhythm on the folder. Time is political capital; you're asking for a currency she wishes she'd never spend."

    menu:
        "Accept terms to secure full funding and relocation aid":
            jump chapter10
        "Refuse and demand a binding pilot with legal protections":
            jump chapter12
        "Leak the contract to force public scrutiny":
            jump chapter16
    return
