label chapter3:

    # [Scene: Tidehaven Boardwalk | Late Afternoon]
    # play sound "sfx_placeholder"  # [Sound: Bell toll, low and distant]
    # play music "music_placeholder"  # [Music: Thin piano, unresolved minor chord]

    scene bg ch3_98c6f2_1 at full_bg
    "You stand with the field jacket pulled tight around your shoulders, the damp pressing through the collar like a question. The bell in the town hall still vibrates in your chest; the meeting is a bruise"
    "beneath your ribs. The harbor is a sheet of pewter, restless and patient. Each creak beneath your boots sounds like a ledger closing and opening at once."
    "The air tastes of old rope and iron; gulls call somewhere beyond the fog but their shapes are only noise. The boardwalk rail is cold where your hand rests. In your palm the town's lines feel"
    "like raised seams—property boundaries, fishing routes, the invisible stitches that hold people to place. You can see them as if on a map: where people fish, where Bento's knees know the shallows, where the younger families"
    "park their boats. Every seam is someone’s history, and every history is a possible loss."
    "You exhale. The compass at your throat—a warm, familiar weight—suddenly feels like a metronome for decisions you didn't ask to make."

    scene bg ch3_98c6f2_2 at full_bg
    "(Narration)"

    "Bento's voice replays in the hallway like gravel" "You left, Mira.' It wasn't accusatory so much as a fact that settled like silt. You don't tidy it away; you let it lie heavy. It sits alongside Asha's steadiness, Jonah’s low-voiced stubbornness, Dr. Lian's charts, and Evelyn's tired request—'Mira—will you shepherd this?"

    menu:
        "Call Jonah now — hear his pitch again":
            "Your thumb hesitates on his number. You imagine his voice, the rasp of the harbor in it, the impatience turned warm if he thinks you're with him. Part of you aches toward that straightforward, neighborly certainty."
        "Return to the lab and run Dr. Lian's models again":
            "You picture the lab's cool light and the teal lines on her maps. Numbers are honest in their own way; they don't offer forgiveness, only projections. The laptop hums in your mind like a small engine of truth."

    # --- merge ---
    "Continue to 'You close the phone without calling. The decision isn't friendly to rush. The fog swallows the screen of your thoughts and the bell tolls again.'"
    "You close the phone without calling. The decision isn't friendly to rush. The fog swallows the screen of your thoughts and the bell tolls again. For a long moment you just listen: the harbor's flat breath,"
    "the distant clank of a mooring line, the creak of an old sign. Every sound becomes an argument in miniature."
    # [Scene: Tidehaven Town Hall — Corridor Outside Council Chamber | Moments Later]
    # play sound "sfx_placeholder"  # [Sound: Distant chatter through the chamber door; footsteps on linoleum]
    # play music "music_placeholder"  # [Music: Low, taut strings]
    "You walk back toward the town hall because leadership is a place that expects you at its thresholds. The corridor smells faintly of coffee and stale paper—petitions pinned like moth wings to the corkboards. Bento is"
    "there, stooped against the wall, hands threaded in each other as if holding the past together. His face has the map of the weather in it."
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "You left, Mira."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I know."
    "Bento Morais: (He studies you.) 'We needed you, girl. The sea doesn't wait for apologies.'"

    mira_kestrel "I didn't think—"

    bento_old_bento_morais "We still do. But it changes your standing when you go and come back. People remember what you chose when the waters rise."
    "You swallow and press your palm to the corridor's cool tile. Bento's hands are like barnacled anchors. He smells of smoked fish and oil smoke; the scent tethers you to a childhood of boat decks and"
    "his stories. You want to tell him how much you carry—how you'd stayed up nights redrawing marsh lines, how you've been trying to reconcile engineering with memory—but the words want to be less clinical and more"
    "human, and you don't know which he'll take as a plan and which as confession."

    menu:
        "Tell Bento you left to learn how to help":
            "His eyes water for a second—friction turning to something like understanding—and then he huffs softly. 'Learning won't stop the sea.' The pause that follows is both warning and blessing."
        "Admit you still feel guilty and ask for his trust":
            "Bento's jaw tightens. He studies your hands, then nods once, slow. 'Trust is earned, Mira. Start earning it.' It sounds like a task; tasks are what he gives you now."

    # --- merge ---
    "Continue to 'You leave Bento with a promise you aren't yet sure you can keep.'"
    "You leave Bento with a promise you aren't yet sure you can keep. His words settle into the lining of your jacket like grit."
    # [Scene: Saltmarsh Research Lab | Early Evening]
    hide bento_old_bento_morais
    hide mira_kestrel

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of servers; distant drip from a condensing pipe]
    # play music "music_placeholder"  # [Music: Sparse, clinical synth underscoring tension]
    "The lab feels colder than the corridor. Here, under LEDs and the clean geometry of maps, the fight turns into numbers. Dr. Lian Zhou stands over a workstation, her palms flat on the table like she’s"
    "steadying herself against the future. The laptop you set on the bench is open to her latest projection: five-year scenarios tracked in jagged teal—wetland area shrinking into sharper teeth with each tick."
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "The models show the marsh stepping back faster than our last run suggested. Salt intrusion accelerates loss if we don't change hydrology.' (She taps a jagged line.) 'That's the baseline without intervention."
    "You lean closer, the light catching the tired curve beneath your eyes. The graphs look inevitable and small at once—numbers that already belonged to futures you refused to name when you were younger."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "How confident are these ranges?"

    dr_lian_zhou "We're within a tight confidence interval for sea-level acceleration and sediment deficits. Intervention windows close—some in as little as three years for certain shoals. We can buy time with soft measures, but only if they're scaled and maintained."
    "Asha Verma enters the lab with her coat clipped at the shoulders, an argument already forming in the angular set of her mouth."
    show asha_verma at center:
        zoom 0.7

    asha_verma "Mira, we can't rely on volunteer crews and pole plantings to hold a coastline when the sea's behaving like a bulldozer. We need enforceable zones, a sea-gate pilot, reinforced berms. I need someone to lead the technical deployment."
    "You look at Asha's eyes—steel-blue and exact. There's no theatrical cruelty there, only a steady, bureaucratic cruelty of necessity that learned its rules through loss."

    mira_kestrel "Enforceable zones mean people uprooted.' (The sentence tastes like salt.) 'Sea-gates mean capital, construction, and political friction. It's not purely technical."
    "Asha Verma: (Quiet but firm.) 'No solution is purely technical, Mira. But neither is this a sentimental choice. If we act slowly, we risk rapid failure. I want someone who can stand in the centre of this and make the hard calls.'"
    "Jonah Reyes appears in the doorway before you can answer, the lab's fluorescent light flattening the warmth in his eyes but not taking it away."
    hide dr_lian_zhou
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Hard calls, yeah. But the town's hands should be on those projects. We know the tides—Bento taught me where poles hold and where they don't. We can rebuild poles and marshes. People will come. We don't need a machine deciding which houses are worth saving."
    "The room shifts with Jonah's entrance: his scent of wool and wet rope, his steady, stubborn warmth against Asha's surgical clarity. The temperature of the conversation drops and bakes in the same moment."

    asha_verma "People die when systems fail, Jonah. Emotion won't stop the waterline."

    jonah_reyes "And policy without people is a graveyard of machines. Who pays for the upkeep when the funding dries? Who takes responsibility when a berm fails? You speak of efficiency; we speak of belonging."
    "Mira Kestrel: (You feel the old ache—guilt braided with determination.) 'Both of you are right and wrong in different ways. Asha, your timeframes are tight—you're trying to prevent collapse. Jonah, your pride in the town's methods"
    "is what keeps the place whole. Dr. Lian, your models close windows. Bento's memory keeps us honest. Evelyn wants a recommendation.'"
    "Evelyn Sato: (Entrances with the tired dignity of someone who must distribute hope with tight hands.) 'Mira. We're listening. Council wants a recommendation by next week. Pilot, maintenance plan, or phased infrastructure. The town waits. You know everyone in this room. What do you recommend?'"
    "The question lands like a tide on rock—patient, inevitable. Outside, the harbor breathes. Inside, the machines hum."
    hide mira_kestrel
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "There's a way to structure pilots to produce defensible data. We can test a living shoreline at one shoal and a managed berm at another. But we need clarity on what success metrics will be used and who will commit to maintenance."

    jonah_reyes "You mean trials. Trials take time. People in the interim will keep losing ground."

    asha_verma "Trials without firm fallback plans create false hope."
    "Mira Kestrel: (You close your eyes because the noise is too loud inside your skull: Bento's small condemnation, your father's ghost on an empty deck, Jonah's camera shutter capturing a harbor that keeps getting smaller, Asha's hard-lipped urgency. The models on your laptop glow behind your eyelids like watchful fish.)"
    "(Narration)"
    "You feel the town as a fault line beneath your boots—one brittle seam where values pull opposite ways. You don't just hold scientific knowledge here; you carry the moral ledger of who pays what cost. Your"
    "hands are maps of past storms: calluses from crawling on decks, the faint scar from a rope that slipped years ago—you remember your father when the boat was taken; you remember leaving. All of that counts"
    "now in a way that charts never capture."

    menu:
        "Ask Dr. Lian to prioritize community-scale metrics over strict engineering KPIs":
            "Dr. Lian looks hesitant but interested. 'We can add participatory metrics—maintenance capacity, volunteer hours, social acceptance—into the model. It will complicate analysis, but yes. It's feasible.' You sense the data shifting toward people."
        "Ask Asha to outline a contingency plan for displaced households":
            "Asha's jaw tightens, then she nods once. 'I'll draft protocols for managed retreat and compensation pathways. It'll be heavy, bureaucratic, but clearer for the council to swallow.' Her competence makes the plan feel colder but more real."

    # --- merge ---
    "Continue to 'You realize that each path will fracture something: a relationship, a tradition, a sense of security.'"
    "You realize that each path will fracture something: a relationship, a tradition, a sense of security. Nothing is purely technical. Nothing is purely sentimental."
    "Asha steps closer, lowering her voice so the wires and monitors cannot overhear her."

    asha_verma "Mira, I need someone who's decisive. This town needs a leader who can navigate politics and spreadsheets. Will you lead the deployment?"
    "Jonah Reyes: (Jonah's hand brushes the back of a chair as if readying himself to stand and plant stakes in the mud, the image of his wrists callused around rope knotting in your chest.)"

    jonah_reyes "If you choose people, you'll be choosing to fight with them. You'll get your hands dirty. You'll also be choosing to take more time—and possibly more risk. But you'll be doing it with people who remember why each stone matters."
    hide asha_verma
    show evelyn_sato at center:
        zoom 0.7

    evelyn_sato "Council needs a single recommendation. The public hearing will be brutal. Whatever you choose, own it or we'll flounder. Tidehaven can't afford a leader who is indecisive."
    "You inhale and the lab's sterile lights feel like a spotlight. The wind beyond the panes feels like an accusation. Your chest tightens as if sea air itself is compressing the space around your heart."
    "(Narration)"
    "You replay every possible outcome like a tide chart—what you salvage, what you concede. You picture Bento walking the reclaimed marsh and nodding or shaking his head. You picture Jonah's hands wrapped around a pole he"
    "helped plant; you picture Asha's plans being drawn up and signed and becoming law. You imagine telling families that their gardens are doomed or that their houses will be moved. The ledger fills with names."
    "A loop of silence pulls taut in your throat. The models on your screen—teal jagged futures—seem to await your signature on the air itself. You are the hinge, and everything leans."
    hide jonah_reyes
    hide dr_lian_zhou
    hide evelyn_sato

    scene bg ch3_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: Single low chord held until it fades]
    "You could split the pilot to test both approaches; you could commit fully to one; you could let the town decide in a messy, human way. Each route is a kind of grief."
    # [Scene Transition: The lab lights dim slightly; the harbor beyond grows more indistinct as evening presses in]
    # play music "music_placeholder"  # [Music: Piano; unresolved]
    "You know the choice you make will set the town's course and reshape what 'home' means for many. The council wants a recommendation. The town waits. Your palms feel like maps of past storms—and of possible futures."

    menu:
        "Stand with Jonah and the community-led living shorelines.":
            jump chapter4
        "Back Asha's decisive infrastructural plan for a sea-gate and reinforced berms.":
            jump chapter7
        "Propose a hybrid: gather stronger community data, pilot both approaches, and broker a phased plan.":
            jump chapter10
    return
