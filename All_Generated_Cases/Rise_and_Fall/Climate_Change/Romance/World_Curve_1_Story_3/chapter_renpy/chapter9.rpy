label chapter9:

    # [Scene: The Promenade | Morning]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady strings with a low cello underpinning]
    # play sound "sfx_placeholder"  # [Sound: Rhythmic thumping of pile-drivers; distant gull calls cut through the diesel hum; people murmuring and a child's laugh]
    "You stand near the temporary staging dock, raincoat sleeves rolled, fingers wrapped around a paper cup that has gone cold. The air tastes of salt and iron, an odd, honest flavor — the city doing what"
    "it can to survive. Around you, neighbors who taught you to splice pumps and bind reeds move with a new kind of purpose: Rani teaching two teenagers to rivet a handrail; elders laying out trays of"
    "marsh-grass plugs like a ceremonial offering."
    "Your chest feels a peculiar lightness; it spreads from your sternum into your hands and down into the boots that have tracked mud through more meetings than you can count. This is not unalloyed joy. It"
    "is relief braided with grief and a stubborn, steady hope — the kind you earn with long hours and quieter compromises."
    show rani_cho at left:
        zoom 0.7

    rani_cho "Look at this — actual, proper hardware. You look good with a hard hat, by the way."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "That's not surprising. I look good getting things done."

    rani_cho "Don't get sappy on me. Will you keep Elias from putting sensors in every plank?"
    show elias_harrow at center:
        zoom 0.7

    elias_harrow "Sensors tell stories, Rani. They tell whether our roots will hold or if we need to change direction. We are listening, not just guessing."
    "You watch him—methodical, patient even here—balancing a tablet and a spool of wire like an instrument. When he looks up, his amber eyes find you, and the wordless agreement there steadies you in the way a good knot steadies a line in a storm."

    "Councilor Mateo Qu (checking a damp packet of papers, voice thin but steady)" "We got the funding through the emergency committee. It wasn't pretty, but the allocations are in. There are provisions for relocation, for maintenance training, for oversight."
    hide rani_cho
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "And the access points were engineered so emergency services can reach critical zones without compromising the main root-mats. It's the only way we met the city's minimal response standards."
    "There is an intake of breath that is almost audible. You remember the nights of shouting into echo chambers, the recorded hearings, the pamphlets handed from frail hands. Part of you tightens at Lucia Montrose's words"
    "— the shape of 'minimal response standards' once meant bulldozers rolled through songlines — but you also remember pleading with Councilors and rowdy town halls until someone listened. This balance is the work of too many"
    "hands."

    "Eda Nal (slow, weathered voice, carrying a woven basket of seed-trays)" "We asked for the land to keep its breath. The engineers have to learn to breathe with it, not over it."

    mara_solenne "We asked for stewardship, not a spectacle. We will keep watch. We will teach maintenance. We will guard how this seed is used."

    lucia_montrose "I can respect that. Beaconworks will fund technician positions from the project pool. We want the model to be replicable — measured, maintained, credited."
    "There is a pause when Lucia Montrose says 'credited.' The city has a shorthand for credit — press releases, plaques, logos on project banners. For a beat, you picture a corporate placard where Eda's hand-sewn sign should be. The thought prickles with familiar indignation."

    menu:
        "Insist we keep only community logos on the main banner":
            "You lift your chin and speak with a voice carved by nights on the pontoon. 'We will not let corporate gloss cover the names of the people who bind this place together.' The technicians exchange glances; Elias' jaw tightens—he appreciates the stance, even if it complicates funding reports."
        "Accept Beaconworks' logo if it guarantees training slots for locals":
            "You allow a measured nod, feeling each concession like a stitch. 'If the logo brings training and jobs for our people, let it be.' Rani gives you a thumbs-up; Lucia gives a curt, almost-pleased smile, and Elias relaxes as the logistical headache shrinks into solvable tasks."

    # --- merge ---
    "Continue"
    "You feel the microchoices of diplomacy — when to hold the line, when to bend it into something useful. This pilot is built of such threads: technical specs and human care woven together."
    # [Scene: Beaconworks Lab | Midday]
    hide mara_solenne
    hide elias_harrow
    hide lucia_montrose

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft clack of keyboards, the low thrum of lab pumps, water trickling from a test tank]
    "Inside Beaconworks, the modular root-mats are tested in a long, clear tank. You stand with Elias Harrow and a Beaconworks Technician as a tray of inserted sediment is lowered and the water is pumped to simulate a spring tide."

    "Beaconworks Technician" "We tuned the mat's porosity; the pylons are designed to flex with surge models. If the sensors report unusual scour, the maintenance drone can attach a temporary anchor until crews arrive."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "And the data will be open — published weekly. We want researchers and neighbors both to see what we learn."

    "You like that phrase" "neighbors both."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Open data, yes. And local oversight. The maintenance trainees will be hired from the Drowned Garden first. Rani's workshops train them to repair the mats and the floats."

    "Beaconworks Technician" "Agreed. We've budgeted stipends for training. Lucia Montrose insisted on measurable outputs; Mateo insisted on legal frameworks. It's messy but it's funded."
    show lucia_montrose at center:
        zoom 0.7

    lucia_montrose "Messy is better than absent."
    "You exchange a look with Elias Harrow — small, private. The conversation slides into the softer, human edges: the names of people in the trainee roster, the schedule for Rani's beginner riveter class, which elder will"
    "lead the first tidal knowledge workshop. Multiple voices layer and rub against one another; friction that refines rather than breaks."

    menu:
        "Write the pilot's first public blurb in plain community language":
            "You take the marker and scribble a short, blunt line: 'We build with the land. We watch over it together.' The room quiets with approval; someone laughs, delighted, at the clarity."
        "Let Beaconworks craft the scientific-language press release, and add a community addendum":
            "You step back and let the lab's PR mechanics roll. 'They'll get the headlines; we get the people to read the addendum,' you say. Elias nods—scientists like the precision; community organizers like the heart. Both might be necessary."

    # --- merge ---
    "Continue"
    "Later, over a cluttered workbench, Lucia Montrose and Eda Nal find themselves standing side by side, unlikely companions. Lucia Montrose's hands are empty; Eda Nal's are stained with peat."
    hide elias_harrow
    show eda_nal at left:
        zoom 0.7

    eda_nal "Our grandmothers braided reeds before there were any plans. Teach them the braided ways and the engineers will learn to hold the braid without breaking it."

    "Lucia Montrose (considering, almost to herself)" "Perhaps the braid will hold better than singular walls."
    "You watch them. A tiny, realignment-possible moment flickers: practical respect, the kind that doesn't dissolve old grievances but softens hard edges."
    # [Scene: Rooftop Market & Greenhouse | Late Afternoon]
    hide mara_solenne
    hide lucia_montrose
    hide eda_nal

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Frying oil, low conversation, the soft clink of seed trays; a distant construction hum]
    "By afternoon, the market is full. Rani's apprentices have set up a modest stall displaying reclaimed-metal planters and stitched waterproof bags — small livelihoods seeded by the pilot's training program. You move through the crowd, accepting"
    "a paper-wrapped fishcake from a vendor, the steam fragrant with ginger. The mood is buoyant, earned."

    "Rani (to a young apprentice)" "Don't overpolish the metal. Let it show where it's been. People like things that wear like stories."

    "Apprentice (beaming)" "My mum says I'm making real work."
    "You feel the currents of change in small things: a consistent income, a reliable maintenance stipend, a new line of trade for those who used to live hand-to-mouth. These are the human scaffolding beneath the technical scaffold."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "I accepted an advisory role with the municipal team. It's... more bureaucracy than romance, but it gives me the seat at the table Lucia Montrose keeps talking about."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "You did? That would mean you could actually steer specifications, not just watch them be written."

    elias_harrow "I want to make sure our modules are implemented the way we designed them. And I want to be able to answer when someone asks why the data looks the way it does. It's work I can do well."
    "You let out a breath that is half laugh, half relieved sob. His choosing a seat inside the machine of the city feels like a tether — not a concession but a form of solidarity that makes the work sustainable."

    mara_solenne "Then let's make sure there is always a person from our neighborhood in those meetings. Promise me that."

    elias_harrow "I promise. And I'll hold you to it."

    "A beat. Then Rani, never one for solemnity, thrusts a small, crudely-cut plaque into your hand" "Pilot Phase One — Drowned Garden Living Barrier."

    menu:
        "Stick this plaque at the base of the first pylon":
            "You smile and secure the plaque on the pylon with a rock and some duct tape, then step back. The technician snaps a photo for the public feed. Later, you see kids pointing at the plaque and asking their parents what it means."
        "Keep the plaque to be placed at the communal garden, with Eda's blessing":
            "You tuck the plaque into your pack. 'We'll put this where people can rest by it,' you tell Rani. Later, Eda lays her hand over the wood and murmurs a blessing. It feels like a small, private victory."

    # --- merge ---
    "Continue"
    # [Scene: The Promenade — First Surge Test | Evening]
    hide elias_harrow
    hide mara_solenne

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Quiet triumphant brass, then a restrained choir of strings]
    # play sound "sfx_placeholder"  # [Sound: The tide's inrush, the slap of waves, a distant rumble of machinery]
    "The city promised a test. A controlled surge simulation, managed pumps and recorded variables. You stand at the edge of the walkway, a circle of hands around yours as others link across the plank. The air"
    "is thick and electric, sea-salt and wet wool; the first spray splashes, cold as truth."

    "Eda Nal (soft)" "This is not the end of the storm. But the land remembers how to keep itself. We are teaching it again."
    "As the synthetic tide pushes, the root-mats flex and breathe with the water, the pylons bow just enough to absorb force. Sensors flicker green on Elias Harrow's tablet; technicians clap as numbers fall within predicted tolerances."
    "An involuntary cry—part cheering, part relief—rises from the crowd. You find yourself laughing, and it becomes a small, clean thing."

    "Lucia Montrose (allowing, at last, a genuine half-smile)" "The models held. Well executed. Council will like quantified success."

    "Mateo (quietly to you)" "We can now argue for scaled funding. This gives us leverage against more destructive proposals."
    "Your heart stutters, not at triumph but at the way triumph mixes with loss. You remember the strips of wetland that were altered for secure access — the reed beds rerouted, three small houses that accepted"
    "relocation funds. You remember the late-night negotiations that promised support for those families; you will check that those promises become practice. The victory here is pragmatic, not total."
    show mara_solenne at left:
        zoom 0.7

    mara_solenne "We did not save everything. Some things changed. But what we built today is not a wall that ignores people. It's an opportunity to keep our way of life—adapted, yes, but lived."

    "Woman (quiet)" "It holds. And we will teach it to hold better."
    "The crowd murmurs agreement. You feel Elias Harrow's hand find yours — not because of the cameras, not for a public gesture, but because both of you have been in the mud and the meetings. His"
    "grip is steady; your fingers fit in the small hollow of his palm. There is tenderness, yes, but mostly there is a companionable resolve: work to be done, next storm to meet, kids to teach."
    "Eda Nal steps forward, pulling from her basket a small bundle: the names of residents who left; the list of the relocated, printed and folded like little prayers. She reads each aloud, voice carrying. When she"
    "pauses to say the names of the wetland groves that could not be preserved intact, there is a mournful hush. People do not look away. This is how you mark loss: by naming it, and by"
    "promising repair where you can."
    "Later, near the community bonfire that Rani insisted on setting despite damp air, you watch children roast small fish. The flames make the faces around them glow like a constellation of weathered, bright intentions."

    "Elias Harrow (soft)" "You did more than keep a fight alive. You made a place where people can work and be paid. Where knowledge passes. Where this—' (he gestures, wide) '—can scale."

    mara_solenne "It still feels fragile."
    show elias_harrow at right:
        zoom 0.7

    elias_harrow "Everything worth keeping does."
    "You let yourself rest in that sentence. The pilot is not a miraculous salvation; it is a beginning with scaffolds, funding, people, and a legal backbone that will keep it from being a flash-in-the-pan. It is a pragmatic victory — not all or nothing, but something resilient and human-built."
    # [Scene: Beaconworks Lab — Night]
    hide mara_solenne
    hide elias_harrow

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant rain, the hiss of ventilation]
    "You and Elias Harrow are alone among schematics. He traces a line on the table where the next phase will extend."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "There will be more negotiations. Mateo will hold hearings. Lucia Montrose will push for efficiency. We'll have to keep pressing for community representation in the procurement process."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "You'll be in there. Will you be safe in there? Will you keep our people from being reduced to checkboxes in an RFP?"

    elias_harrow "I can only promise to speak the truth I see and to push for people at every meeting. I can't promise outcomes. But I can be a lever."
    "You study his profile, lit by lab light — skepticism softened into a thing that keeps wanting to build. You feel the tiredness around your mouth and the corners of his eyes; both of you carry"
    "the trace of late nights and harder fights. Yet between those lines there is a rhythm: reports, teaching sessions with Rani, monthly maintenance checks, a published dashboard where anyone can see tide impacts and repair logs."

    mara_solenne "We keep our watch. We keep our schools in the pilot. We demand living wages for maintenance. We make sure the relocated families have job placements."

    elias_harrow "And we teach every engineer who comes through Beaconworks to listen first. Not as a slogan — as a rule."
    "You nod. It feels like an oath. Small, practical vows that stitch the future together one careful choice at a time."

    mara_solenne "Promise me one small thing: when you're tired of meetings, come back to this roof. We'll plant something stupid and persistent. A marsh grass rebellion."

    elias_harrow "I'll come. Bring a shovel."
    "You laugh. It is good to laugh. The city outside remains messy and political and necessary, but in these small domestic promises lies the architecture of a life steady enough to continue the work."
    # [Final Scene: The Drowned Garden — Nightfall]
    hide elias_harrow
    hide mara_solenne

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A warm, conclusive swell — strings and a solo flute]
    "You walk the length of the new living barrier under the string lights. Children play along the edges; elders barter seeds. Someone has left a small carved canoe — a makeshift shrine — filled with marsh"
    "grass and the bronze key from Elias Harrow's pocket chain (he claims he misplaced it; you know he lent it for luck). Rani teases you about your new 'community planning hair' and Eda Nal pulls you"
    "both into the circle as she distributes small paper lanterns."

    "Eda Nal (softly, as she lights the lanterns)" "For what has been kept, and for what will be rebuilt."
    "You let the lantern float; it glows and catches the dark. The pilot is not complete. There will be council disputes. There will be petitions and audits and nights of worry. But you can measure one"
    "thing: tonight, a small community is safer, and several livelihoods are steady. The relocated families have been given funds and placements that Rani and the trainees helped secure. That is not everything, but it is necessary."
    "Elias Harrow squeezes your hand. 'We did it,' he says, not triumphantly but with the simple accuracy of a report."
    "You close your fingers around his. 'We did the work,' you correct, thinking of Rani's riveters, Eda Nal's names, the Beaconworks technicians who stayed late, Lucia Montrose's grudging collaboration, Mateo's procedural gray that somehow opened a window when you most needed it. 'We did the work together.'"
    "He leans in, forehead to yours for a brief, unadorned measure. There is a tenderness to it that feels like a tool — not sentimental, but practical: a steadying touch that will matter when storms return."
    "You breathe in the wet lantern air, in the smell of fried food and damp wood and human skin warmed by shared labor. You think of the reeds and the machines, of the legal papers and"
    "the apprenticeship names, of the things altered and the things saved. The cost of change sits in your bones as surely as the satisfaction of a day where numbers and people matched, if only for a"
    "while."

    "You say aloud, because some victories must be spoken" "We will keep fighting, but for now — tonight — we rest."
    "Around you, the sound of the neighborhood rising into laughter, conversation, and a little more hope answers. The pilot will evolve; the law will be tested; some losses will linger. But this is a pragmatic victory — not a perfect one, but one with a heartbeat."
    # play music "music_placeholder"  # [Music: The strings swell into a hopeful, lingering chord. The rain lightens to a mist. The camera pulls back over the glowing walkways and the washed city beyond, revealing the living threads you've helped stitch into the shore.]

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch9_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
